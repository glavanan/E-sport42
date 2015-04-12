from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth import authenticate, login, logout
from base.forms import UserCreationForm
from base.models import MyUser
from base.models import Tournament, Phase, Teams
from base.serializers import MyUserSerializer, LoginSerializer, TournamentSerializer, TeamSerializer
from base.permissions import IsAccountOwner, IsOwnerOrAdmin
from rest_framework import permissions, viewsets, status, views, permissions
from rest_framework.response import Response
from post.permissions import IsAdminOfSite


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class=TournamentSerializer
    lookup_field = 'id'
    def get_permissions(self):
        return (IsAdminOfSite() if self.request.method == 'GET' else permissions.IsAdminUser(),)

    def create(self, request, **kwargs):
        print "viewset"
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            type = serializer.validated_data.pop('type')
            tournoi = serializer.save()
            for val in type:
                tmp = Phase(tmp_name=val, tournament=tournoi)
                tmp.save()
            print tournoi.phase_set.all()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all()

    serializer_class=TeamSerializer

    def get(self, request):
        Teams.objects.all().order_by('tournoi')
        return Response({}, status=status.HTTP_200_OK)

    def post(self, request):
        print "HEREMOTHERFUCKER"
        serializer = TeamSerializer(data=request.data)
        for data in serializer.data:
            print data
        print "HEREMOTHERFUCKER"
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        print request.data
        team = serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

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

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.update(instance, serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(views.APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        account = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
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

class IndexView(TemplateView):
    template_name = 'user/index.html'