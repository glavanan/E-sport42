from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth import authenticate, login, logout
from base.forms import UserCreationForm
from base.models import MyUser
from base.serializers import MyUserSerializer
from base.permissions import IsAccountOwner
from rest_framework import permissions, viewsets, status, views, permissions
from rest_framework.response import Response


class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    lookup_field = 'username'
    print 'LOLOLOL'

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), IsAccountOwner(), )

    def create(self, request, **kwargs):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid() and request.data['password1'] == request.data['password2']:
            MyUser.objects.create_user(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response({'status' : 'Bad request',
                         'message' : 'User could not be created with received data.'}, status=status.HTTP_400_BAD_REQUEST)
    # def list(self, request, *args, **kwargs):
    # 	obj = []
    # 	for i in self.queryset:
    # 		i[]
    # 	print obj
    # 	return Response({'lol': 'prout'})

class LoginView(views.APIView):
    def post(self, request, format=None):
        data = request.data
        print data.get("username", None)
        print request.body
        username = data.get('username', None)
        password = data.get('password', None)
        account = authenticate(username=username, password=password)
        if account is not None:
            login(request, account)
            serializers = MyUserSerializer(account)
            serializers.data['is_logged'] = True
            return Response(serializers.data)
        else:
            return Response({'status' : 'Unauthorized',
                'message' : 'usernamen/password combination invalid'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, format=None):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class IndexView(TemplateView):
    template_name = 'user/index.html'