from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from match.serializer import MatchSerializer
from match.models import Match
from match.permissions import IsAdminTournament
from tournoi.models import Phase
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import detail_route
import math

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def get_queryset(self):
        return Match.objects.filter(phase=self.kwargs['parent_lookup_phase'])

    def get_permissions(self):
        self.request.ID = self.kwargs['parent_lookup_tournoi']
        if self.request.method == 'GET':
            return [permissions.AllowAny(),]
        if self.request.method == 'POST':
            return [IsAdminTournament(), ]
        return [permissions.IsAdminUser(), ]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            match = serializer.save(phase=Phase.objects.get(id=1))
            serializer.validated_data['team1'] = serializer.validated_data['team1'].id
            serializer.validated_data['team2'] = serializer.validated_data['team2'].id
            serializer.validated_data['phase'] = match.phase.id
            return Response(serializer.validated_data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['post'])
    def end_match(self, request, pk=None, parent_lookup_tournoi=None, parent_lookup_phase=None):
        match = Match.objects.get(id=pk)
        match.end = True
        tournoi = match.phase.tournament
        round_max = int(math.ceil(math.log(tournoi.nbteams, 2)))
        if match.phase.name == 'DTree':
            if match.looser_braket == False:
                if match.level < round_max:
                    n_winner = match.match_number / 2
                    l_winner = match.level + 1
                    n_looser = match.match_number
                    l_looser = match.level
                else:
                    n_winner = 0
                    l_winner = round_max
                    n_looser = 0
                    l_looser = round_max + 0.5
                next_match_w = Match.objects.get(match_number=n_winner, level=l_winner, phase=match.phase, looser_braket=True if match.level==round_max else False)
                if match.match_number % 2 == 0:
                    next_match_w.team1=match.team1 if match.score_t1 > match.score_t2 else match.team2
                else:
                    next_match_w.team2=match.team1 if match.score_t1 > match.score_t2 else match.team2
                next_match_w.save()
                next_match_l = Match.objects.get(match_number=n_looser, level=l_looser, phase=match.phase, looser_braket=True)
                next_match_l.team1=match.team1 if match.score_t1 < match.score_t2 else match.team2
                next_match_l.save()
            else:
                if match.level == 0:
                    n_winner = match.match_number
                    l_winner = 1
                elif match.level % 1 == 0:
                    n_winner = match.match_number
                    l_winner = match.level + 0.5
                else:
                    n_winner = (match.match_number - match.match_number%2)/2
                    l_winner = match.level + 0.5
                next_match_w = Match.objects.get(match_number=n_winner, level=l_winner, phase=match.phase, looser_braket=True)
                if match.level % 1 != 0 or (match.match_number % 2 != 0) or match.level == 0:
                    next_match_w.team2=match.team1 if match.score_t1 > match.score_t2 else match.team2
                else:
                    next_match_w.team1=match.team1 if match.score_t1 > match.score_t2 else match.team2
                next_match_w.save()
        elif match.phase.name == 'Pool':

        match.save()
        return Response({"Match" : "ok"}, status.HTTP_200_OK)