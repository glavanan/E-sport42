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
from base.permissions import IsAccountOwner, IsOwnerOrAdmin
from rest_framework import permissions, viewsets, status, views, permissions
from rest_framework.response import Response


class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    lookup_field = 'username'
    permission_classes = (IsOwnerOrAdmin, permissions.IsAuthenticated)

    def create(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            MyUser.objects.create_user(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(views.APIView):
    def post(self, request, format=None):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        if not username or not password:
            return Response({"error": "Missing parameters"}, status=status.HTTP_400_BAD_REQUEST)
        user = MyUser.objects.filter(username=username)
        if not user:
            return Response({"error": "Unknown user"}, status=status.HTTP_404_NOT_FOUND)
        print password
        account = authenticate(username=username, password=password)
        if account is not None:
            login(request, account)
            serializers = MyUserSerializer(account)
            return Response(serializers.data)
        else:
            return Response({'error': 'Invalid password for this user'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, format=None):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class UserExists(views.APIView):

    def get(self, request, format=None):
      try:
        if request.method == 'GET':
            data = request.GET['username']
            data1 = request.GET['email']
            print data
            user = MyUser.objects.filter(username=data)
            email = MyUser.objects.filter(email=data1)
            emailr = False
            if email:
                emailr = True
            userr = False
            if user:
                userr= True
            return Response({"user" : userr, "email" : emailr})
      except:
        return Response({"message" : "un post ?"})
    def post(selfself, request, format=None):
        data = request.data
        user = MyUser.objects.filter(username=data.get('username', None))
        email = MyUser.objects.filter(email=data.get('email', None))
        emailr = False
        if email:
            emailr = True
        userr = False
        if user:
            userr= True
        return Response({"user" : userr, "email" : emailr})

class IndexView(TemplateView):
    template_name = 'user/index.html'