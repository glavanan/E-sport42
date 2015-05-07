from django.shortcuts import render
from rest_framework.response import Response
from tournoi.models import Tournament, Teams, Phase, TPost, APost
from tournoi.serializers import TournamentSerializer, TeamSerializer, TPostSerializer, APostSerializer
from post.permissions import IsAdminOfSite, IsTornamentOrAdmin
from rest_framework import permissions, viewsets, status, views, permissions
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
            print "is tornament"
            return (IsTornamentOrAdmin(), )
        except:
            print ("not int")
            if self.request.method == 'GET' or self.request.method == 'POST':
                return [permissions.AllowAny(), ]
            return [IsAdminOfSite(), ]

    def create(self, request, **kwargs):
        print "viewset"
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            type = serializer.validated_data.pop('type')
            tournoi = serializer.save()
            for val in type:
                tmp = Phase(tmp_name=val, tournament=tournoi)
                tmp.save()
            print tournoi.phase_set.all()
            #Je doit retourenr le validated data - User !!!
            return Response({"ok" : "done"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all()

    serializer_class=TeamSerializer

    def get_queryset(self):
        return Teams.objects.filter(tournament=self.kwargs['parent_lookup_tournoi'])
    def post(self, request):
        print "HEREMOTHERFUCKER"
        serializer = TeamSerializer(data=request.data)
        for data in serializer.data:
            print data
        print "HEREMOTHERFUCKER"
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        print request.data
        team = serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
# Create your views here.
