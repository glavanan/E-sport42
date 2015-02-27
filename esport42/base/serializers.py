from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from base.models import MyUser


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('id', 'email', 'username', 'created_at', 'updated_at',
                  'first_name', 'last_name', 'address', 'password1',
                  'password2', 'birth_date', 'nationality', 'phone')
        read_only_fields = ('username', 'first_name', 'last_name', 'created_at', 'updated_at',)

        def create(self, validated_data):
            return MyUser.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.address = validated_data.get('address', instance.address)
            instance.email = validated_data.get('email', instance.email)
            instance.phone = validated_data.get('phone', instance.phone)
            instance.nationality = validated_data.get('nationality', instance.nationality)



            instance.save()

            password1 = validated_data.get('password1', None)
            password2 = validated_data.get('password2', None)

            if password1 and password2 and password1 == password2:
                instance.set_password(password1)
                instance.save()

            update_session_auth_hash(self.context.get('request'), instance)

            return instance