from tournoi.models import Tournament, Teams, TPost, APost
from base.serializers import MyUserSerializer
from rest_framework import serializers

class TournamentSerializer(serializers.ModelSerializer):
    type = serializers.ListField(child=serializers.CharField(max_length=20), write_only=True)
    class Meta:
        model = Tournament
        fields = ('id', 'name', 'nbteams', 'template', 'type', 'player_per_team', 'admin')
        read_only_fields = ('id')

class TeamSerializer(serializers.ModelSerializer):
#Hey pede tu a pas reussis a resoudre le probleme regarde si il y a pas un serializer.ququechose, cadeau :
#http://www.django-rest-framework.org/api-guide/serializers/#writable-nested-representations
    class Meta:
        model = Teams
        fields = ('name', 'members', 'tournoi')
    def create(self, validated_data):
        users = validated_data.pop('members')
        team = Teams.objects.create(**validated_data)
        for man in users:
            team.members.add(man)
        return team

class APostSerializer(serializers.ModelSerializer):
    author = MyUserSerializer(read_only=True, required=False)

    class Meta:
        model = APost
        fields = ('id', 'author', 'title', 'created_at', 'updated_at',  'content')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusion(self):
            exclusions = super(TPostSerializer, self).get_validation_exclusions()
            return exclusions + ['author', 'tournament']

class TPostSerializer(serializers.ModelSerializer):
    author = MyUserSerializer(read_only=True, required=False)

    class Meta:
        model = TPost
        fields = ('id', 'author', 'title', 'created_at', 'updated_at',  'content', 'image')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusion(self):
            exclusions = super(TPostSerializer, self).get_validation_exclusions()
            return exclusions + ['author', 'tournament']