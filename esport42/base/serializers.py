from django.contrib.auth import update_session_auth_hash, authenticate

from rest_framework import serializers

from base.models import MyUser
from base.models import Tournament, Teams


class TournamentSerializer(serializers.ModelSerializer):
    type = serializers.ListField(child=serializers.CharField(max_length=20), write_only=True)
    class Meta:
        model = Tournament
        fields = ('id', 'name', 'nbteams', 'template', 'type', 'player_per_team')
        read_only_fields = ('id')






class MyUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password_confirm = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = MyUser
        fields = ('id', 'email', 'username', 'created_at', 'updated_at',
                  'first_name', 'last_name', 'address', 'birth_date',
                  'nationality', 'phone', 'password', 'password_confirm')
        read_only_fields = ('created_at', 'updated_at')

    def create(self, validated_data):
        return MyUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.nationality = validated_data.get('nationality', instance.nationality)
        instance.save()

        password = validated_data.get('password', None)
        password_confirm = validated_data.get('password_confirm', None)

        if password and password_confirm and password == password_confirm:
            instance.set_password(password)
            instance.save()

        update_session_auth_hash(self.context.get('request'), instance)
        return instance

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



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate_username(self, value):
        if not MyUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("User does not exists")
        return value

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if not user:
            raise serializers.ValidationError("Password don't match with this username")
        return attrs
