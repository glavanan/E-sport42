from django.shortcuts import render
from rest_framework.response import Response
from tournoi.models import Tournament, Teams, Phase, TPost, APost
from tournoi.serializers import TournamentSerializer, TeamSerializer, TPostSerializer, APostSerializer
from post.permissions import IsAdminOfSite, IsTornamentOrAdmin
from rest_framework import permissions, viewsets, status, views, permissions
import urllib
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.generic import View
from rest_framework.decorators import detail_route
from django.core import serializers
from rest_framework.renderers import JSONRenderer

class APostViewSet(viewsets.ModelViewSet):
    queryset = APost.objects.all()
    serializer_class = APostSerializer
    lookup_field = 'id'
    def get_queryset(self):
        return APost.objects.filter(tournament=self.kwargs['parent_lookup_tournoi'])
    def get_permissions(self):
        self.request.ID = self.kwargs['parent_lookup_tournoi']
        if self.request.method == 'GET':
            return [permissions.AllowAny(),]
        else:
            return [IsTornamentOrAdmin(),]
    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user, tournament=Tournament.objects.get(id=self.kwargs['parent_lookup_tournoi']))
        return super(APostViewSet, self).perform_create(serializer)


class TPostViewSet(viewsets.ModelViewSet):
    queryset = TPost.objects.all()
    serializer_class = TPostSerializer
    lookup_field = 'id'
    def get_queryset(self):
        return TPost.objects.filter(tournament=self.kwargs['parent_lookup_tournoi'])
    def get_permissions(self):
        self.request.ID = self.kwargs['parent_lookup_tournoi']
        if self.request.method == 'GET':
            return [permissions.AllowAny(),]
        else:
            return [IsTornamentOrAdmin(),]
    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user, tournament=Tournament.objects.get(id=self.kwargs['parent_lookup_tournoi']))
        return super(TPostViewSet, self).perform_create(serializer)


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    lookup_field = 'id'

    def get_permissions(self):
        url = self.request.build_absolute_uri()
        part = url.split('/')
        try:
            int(part[-2])
            return (IsTornamentOrAdmin(), )
        except:
            if self.request.method == 'GET':
                return [permissions.AllowAny(), ]
            elif self.request.method == 'POST':
                return [permissions.IsAuthenticated(), ]
            return [IsAdminOfSite(), ]

    def create(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            type = serializer.validated_data.pop('type')
            tournoi = serializer.save()
            for val in type:
                tmp = Phase(tmp_name=val, tournament=tournoi)
                tmp.save()
            #Je doit retourenr le validated data - User !!!
            return Response({}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all()

    serializer_class = TeamSerializer

    def get_queryset(self):
        return Teams.objects.filter(tournament=self.kwargs['parent_lookup_tournoi'])
    def get_permissions(self):
        self.request.ID = self.kwargs['parent_lookup_tournoi']
        if self.request.method == 'GET':
            return [permissions.AllowAny(),]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated(), ]
        else:
            return [IsAdminOfSite(),]

    def perform_create(self, serializer):
        serializer.save(tournament=Tournament.objects.get(id=self.kwargs['parent_lookup_tournoi']))
        return super(TeamsViewSet, self).perform_create(serializer)

    def create(self, request, **kwargs):
        serializers = self.serializer_class(data=request.data)
        tournoi = Tournament.objects.get(id=self.kwargs['parent_lookup_tournoi'])
        if serializers.is_valid():
            if len(serializers.validated_data['members']) >= tournoi.player_per_team - 1 and len(serializers.validated_data['members']) <= tournoi.max_player - 1:
                serializers.save(tournament=tournoi)
                serializers.validated_data.pop('members')
                serializers.validated_data.pop('admin')
                return Response(serializers.validated_data, status=status.HTTP_201_CREATED)
            return Response({"error" : "Not enough member"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)





@csrf_exempt
def ipn(request):
    if request.method == 'POST':
        print 'POST'
        print request.POST
        data = dict(request.POST)
        print 'cmd=_notify-validate&' + urllib.urlencode(data)
        tmp = urllib.urlopen("https://www.sandbox.paypal.com/cgi_bin/websrc", 'cmd=_notify-validate&' + urllib.urlencode(data)).read()
        if tmp == 'VERIFIED':
            if data('payement_status') == 'Completed':
                Teams.objects.filter(txn_id=data('txn_id'))
                team = Teams.objects.filter(id=data('custom'))
                if not Teams.objects.filter(txn_id=data('txn_id')) and data('receiver_email') == team.tournament.receiver_email and data('mc_gross') == team.tournament.price and data('payment_status') == 'Completed' and data('mc_currency') == 'EUR':
                    team.verified = True
                    team.txn_id = data('txn_id')
                    team.save()
                    print "gg"
                print "almost"
        else:
            print "ret"
            print tmp
            print "fail"
        return HttpResponse("OK")
    else:
        return HttpResponse('<form method="post" action="https://www.sandbox.paypal.com/cgi-bin/webscr" class="paypal-button" target="_top" style="opacity: 1;"><div class="hide" id="errorBox"></div><input type="hidden" name="button" value="buynow"><input type="hidden" name="business" value="42.esport1@gmail.com"><input type="hidden" name="item_name" value="tournoi"><input type="hidden" name="quantity" value="1"><input type="hidden" name="amount" value="50"><input type="hidden" name="currency_code" value="EUR"><input type="hidden" name="shipping" value="0"><input type="hidden" name="tax" value="0"><input type="hidden" name="notify_url" value="127.0.0.1/api/v1/ipn"><input type="hidden" name="env" value="www.sandbox"><input type="hidden" name="cmd" value="_xclick"><input type="hidden" name="bn" value="JavaScriptButton_buynow"><input type="hidden" name="custom" value="1"/><button type="submit" class="paypal-button large">Buy Now</button></form>')

class TeamExists(views.APIView):
    def get(self, request):
        teamname = request.GET.get('name', None)
        tournament = request.GET.get('tournament', None)
        print tournament
        if teamname and tournament and not Teams.objects.filter(name=teamname, tournament=tournament):
            return Response({}, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

class TagExists(views.APIView):
    def get(self, request):
        teamname = request.GET.get('name', None)
        tournament = request.GET.get('tournament', None)
        print tournament
        if teamname and tournament and not Teams.objects.filter(tag=teamname, tournament=tournament):
            return Response({}, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

# Create your views here.
