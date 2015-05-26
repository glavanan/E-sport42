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
            if self.request.method == 'GET' or self.request.method == 'POST':
                return [permissions.AllowAny(), ]
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
        if self.request.method == 'GET' or self.request.method == "POST":
            return [permissions.AllowAny(),]
        else:
            return [IsAdminOfSite(),]
    def perform_create(self, serializer):
        serializer.save(tournament=Tournament.objects.get(id=self.kwargs['parent_lookup_tournoi']))
        return super(TeamsViewSet, self).perform_create(serializer)


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
                if data('receiver_email') == "esport.42@gmail.com" and data('payment'):
                    print "gg"
        else:
            print "ret"
            print tmp
            print "fail"
        return HttpResponse("OK")
    else:
        data = {}
        site = requests.post('http://127.0.0.1:8000/api/v1/ipn', data=data)
        print site
        return HttpResponse("How the hell did you arrived here ?")


# Create your views here.
