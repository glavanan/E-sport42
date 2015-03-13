from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth import authenticate, login, logout
from base.forms import UserCreationForm
from base.models import MyUser
from base.serializers import MyUserSerializer, LoginSerializer
from base.permissions import IsAccountOwner, IsOwnerOrAdmin
from rest_framework import permissions, viewsets, status, views, permissions
from rest_framework.response import Response


class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    lookup_field = 'username'

    def get_permissions(self):
        return ((permissions.AllowAny() if self.request.method == 'POST'
                else IsOwnerOrAdmin()),)

    def create(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            MyUser.objects.create_user(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(views.APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # data = request.data
        # username = data.get('username', None)
        # password = data.get('password', None)
        # if not username or not password:
        #     return Response({"error": "Missing parameters"}, status=status.HTTP_400_BAD_REQUEST)
        # user = MyUser.objects.filter(username=username)
        # if not user:
        #     return Response({"error": "Unknown user"}, status=status.HTTP_404_NOT_FOUND)
        account = authenticate(username=serializer.validated_data['username'] , password=serializer.validated_data['password'])
        login(request, account)
        serializers = MyUserSerializer(account)
        return Response(serializers.data)

class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, format=None):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)


class UserExists(views.APIView):
    def get(self, request):
        username = request.GET.get('u', None)
        if username and not MyUser.objects.filter(username=username):
            return Response({}, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

class EmailExists(views.APIView):
    def get(self, request):
        email = request.GET.get('e', None)
        if email and not MyUser.objects.filter(email=email):
            return Response({}, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

class IndexView(TemplateView):
    template_name = 'user/index.html'