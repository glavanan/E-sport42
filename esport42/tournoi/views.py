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
from django.shortcuts import redirect
from django.views.generic import View
from rest_framework.decorators import detail_route
from django.core import serializers
from rest_framework.renderers import JSONRenderer
import logging
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


class APostViewSet(viewsets.ModelViewSet):
    queryset = APost.objects.all()
    serializer_class = APostSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return APost.objects.filter(tournament=self.kwargs['parent_lookup_tournoi'])

    def get_permissions(self):
        self.request.ID = self.kwargs['parent_lookup_tournoi']
        if self.request.method == 'GET':
            return [permissions.AllowAny(), ]
        else:
            return [IsTornamentOrAdmin(), ]

    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user,
                                   tournament=Tournament.objects.get(id=self.kwargs['parent_lookup_tournoi']))
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
            return [permissions.AllowAny(), ]
        else:
            return [IsTornamentOrAdmin(), ]

    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user,
                                   tournament=Tournament.objects.get(id=self.kwargs['parent_lookup_tournoi']))
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
            # Je doit retourenr le validated data - User !!!
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
            return [permissions.AllowAny(), ]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated(), ]
        else:
            return [IsAdminOfSite(), ]

    def perform_create(self, serializer):
        serializer.save(tournament=Tournament.objects.get(id=self.kwargs['parent_lookup_tournoi']))
        return super(TeamsViewSet, self).perform_create(serializer)

    def create(self, request, **kwargs):
        serial = self.serializer_class(data=request.data)
        tournoi = Tournament.objects.get(id=self.kwargs['parent_lookup_tournoi'])
        if serial.is_valid():
            if len(serial.validated_data['members']) >= tournoi.player_per_team - 1 and len(
                    serial.validated_data['members']) <= tournoi.max_player - 1:
                serial.save(tournament=tournoi)
                serial.validated_data['members'] = [user.id for user in serial.validated_data['members']]
                serial.validated_data['admin'] = serial.validated_data['admin'].id
                serial.validated_data['tournament'] = tournoi.id
                serial.validated_data['id'] = serial.data['id']
                return Response(serial.validated_data, status=status.HTTP_201_CREATED)
            return Response({"error": "Not enough member"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def ipn(request):
    if request.method == 'POST':
        data = dict(request.POST)
        for k in data:
            data[k] = data[k][0].encode('utf-8')
        tmp = urllib.urlopen("https://www.sandbox.paypal.com/cgi_bin/websrc",
                             'cmd=_notify-validate&' + urllib.urlencode(data)).read()
        if tmp == 'VERIFIED':
            if data['payment_status'] == 'Completed':
                team = Teams.objects.get(id=int(data['custom']))
                if not Teams.objects.filter(txn_id=data['txn_id']) and data[
                    'receiver_email'] == team.tournament.receiver_email and float(data['mc_gross']) == float(
                        team.tournament.price) and data['payment_status'] == 'Completed' and data[
                    'mc_currency'] == 'EUR':
                    team.verified = True
                    team.txn_id = data['txn_id']
                    team.save()
                    send_mail('Paiement tournoi recu',
                              'Nous avons bien recus votre paiement pour le tournoi.  nous vous invitons a etre present aux horraire indiquer sur la page du tournoi. Merci pour votre inscription, et bon tournoi',
                              '42.esport@gmail.com', [team.admin.email])
                    return HttpResponse("team verified")
                logger.debug("almost")
                return HttpResponse("team not valide")
        else:
            logger.debug("ret")
        return HttpResponse("OK")
    else:
        logger.debug("get")
        return HttpResponse(
            '<form method="post" action="https://www.sandbox.paypal.com/cgi-bin/webscr" class="paypal-button" target="_top" style="opacity: 1;"><div class="hide" id="errorBox"></div><input type="hidden" name="button" value="buynow"><input type="hidden" name="business" value="42.esport1@gmail.com"><input type="hidden" name="item_name" value="tournoi"><input type="hidden" name="quantity" value="1"><input type="hidden" name="amount" value="50"><input type="hidden" name="currency_code" value="EUR"><input type="hidden" name="shipping" value="0"><input type="hidden" name="tax" value="0"><input type="hidden" name="notify_url" value="http://danstonpi.eu/api/ret/ipn"><input type="hidden" name="cancel_url" value="http://danstonpi.eu/cancel"><input type="hidden" name="return_url" value="http://danstonpi.eu/done"><input type="hidden" name="cmd" value="_xclick"><input type="hidden" name="bn" value="JavaScriptButton_buynow"><input type="hidden" name="custom" value="26"/><button type="submit" class="paypal-button large">Buy Now</button></form>')

@csrf_exempt
def ipn_return(request):
    if request.method == "POST":
        team = request.POST['custom']
        if team:
            team = Teams.objects.get(id=int(team))
        else:
            return redirect(request.get_host())
        return redirect("http://" + request.META['HTTP_HOST'] + "/tournaments/" + team.tournament.name + "/register-success?teamName=" + team.name)
    elif request.method == "GET":
        return HttpResponse(request.get_host())
    else:
        return redirect(request.get_host())



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
