from django.shortcuts import render
from rest_framework.response import Response
from tournoi.models import Tournament, Teams, Phase
from tournoi.serializers import TournamentSerializer, TeamSerializer
from post.permissions import IsAdminOfSite
from rest_framework import permissions, viewsets, status, views, permissions





class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class=TournamentSerializer
    lookup_field = 'id'
    def get_permissions(self):
        return (IsAdminOfSite() if self.request.method == 'GET' else permissions.IsAdminUser(),)

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
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all()

    serializer_class=TeamSerializer

    def get(self, request):
        Teams.objects.all().order_by('tournoi')
        return Response({}, status=status.HTTP_200_OK)

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
