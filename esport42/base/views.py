from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth import authenticate, login, logout
from base.forms import UserCreationForm
from base.models import MyUser, Payments
from tournoi.models import Teams, Tournament
from base.serializers import MyUserSerializer, LoginSerializer, LimitedMyUserSerializer, PaymentsSerializer
from tournoi.serializers import TournamentSerializer, TeamSerializer
from base.permissions import IsAccountOwner, IsOwnerOrAdmin
from rest_framework import permissions, viewsets, status, views, permissions
from rest_framework.response import Response
from post.permissions import IsAdminOfSite
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer
from django.core.mail import EmailMessage
import logging
from rest_framework.generics import CreateAPIView
logger = logging.getLogger(__name__)

class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    # TODO username to ID

    def get_serializer_class(self):
        try:
            url = self.request.build_absolute_uri()
            url.split('/')
            int(url[-1])
            return MyUserSerializer
        except:
            if self.request.method == 'GET' and not self.request.user.is_staff:
                return LimitedMyUserSerializer
            else:
                return MyUserSerializer


    def get_permissions(self):
        return ((permissions.AllowAny() if self.request.method == 'POST'
                else IsOwnerOrAdmin()),)

    def create(self, request, **kwargs):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        if serializer.is_valid():
            ret = MyUser.objects.create_user(**serializer.validated_data)
            Token.objects.create(user=ret)
            serializer.validated_data['id'] = ret.id
            msg = EmailMessage(subject="Inscription valide", from_email="noreply@esport.42.fr", to=[ret.email])
            msg.global_merge_vars={'NAME1' : ret.username, 'PASSWORD1' : serializer.validated_data['password']}
            msg.template_name="inscription-site-1"
            msg.send()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, *args, **kwargs):
        partial = False
        user = MyUser.objects.get(id=request.data['id'])
        if 'PATCH' in request.method:
            partial = True
        instance = self.get_object()
        request.data['username'] = user.username
        request.data['id'] = user.id
        serializer = self.get_serializer_class()
        serializer = serializer(instance, data=request.data, context={'request': request}, partial=partial)
        if 'password' in request.data and not request.data['password']:
            serializer.exclude_fields(['password'])
        if 'password_confirm' in request.data and not request.data['password_confirm']:
            serializer.exclude_fields(['password_confirm'])
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_202_ACCEPTED)

        # instance = self.get_object()
        # serializer = self.serializer_class(instance, data=request.data, context={'request': request})
        # if serializer.is_valid():
        #     serializer.update(instance, serializer.validated_data)
        #     return Response(serializer.validated_data, status=status.HTTP_202_ACCEPTED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        return self.partially_update(request, *args, **kwargs)

class LoginView(views.APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        account = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        login(request, account)
        token = Token.objects.get(user=account)
        serializers = MyUserSerializer(account)
        data = serializers.data
        data = dict(data)
        data['token'] = token.key
        return Response(data)

class PaymentView(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, format=None):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class UserExists(views.APIView):
    def get(self, request):
        username = request.GET.get('username', None)
        if username and not MyUser.objects.filter(username=username):
            return Response({}, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

class EmailExists(views.APIView):
    def get(self, request):
        email = request.GET.get('email', None)
        if email and not MyUser.objects.filter(email=email):
            return Response({}, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

class NotFound(views.APIView):
    def get(self, request):
        return Response({}, status=status.HTTP_404_NOT_FOUND)

class HomeView(TemplateView):
    template_name = 'user/index.html'

class IndexView(TemplateView):
    template_name = 'user/HOTL.html'
