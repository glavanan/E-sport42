from rest_framework import serializers
from match.models import Match

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('id', 'team1', 'team2', 'phase', 'score_t1', 'score_t2', 'end', 'level', 'match_number')
        read_only_fields = ('id', 'phase', 'level', 'match_number')