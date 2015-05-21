from django.contrib.auth import update_session_auth_hash, authenticate

from rest_framework import serializers
from base.models import MyUser
from tournoi.models import Teams
from tournoi.models import Tournament


class MyUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password_confirm = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = MyUser
        fields = ('id', 'email', 'username', 'created_at', 'updated_at',
                  'first_name', 'last_name', 'address', 'birth_date',
                  'nationality', 'phone', 'password', 'password_confirm', 'is_admin', 'is_staff')
        read_only_fields = ('created_at', 'updated_at', 'is_admin', 'is_staff')

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

    def exclude_fields(self, fields_to_exclude=None):
        if isinstance(fields_to_exclude, list):
            for f in fields_to_exclude:
                f in self.fields.fields and self.fields.fields.pop(f) or next()

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
