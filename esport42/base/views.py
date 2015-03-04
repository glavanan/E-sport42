from django.shortcuts import render
from django.http import JsonResponse
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
import json

class RegisterUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

#class RegisterExtendForm(ModelForm):
#	class Meta:
#		model = Extend
#		fields = ['address', 'nationality', 'phone', 'birth_date']

def register(request):
    if request.method == 'POST':
        form_user = UserCreationForm(request.POST)
        if form_user.is_valid():
            ret = MyUser.objects.create_user(request.POST)
            user = MyUser.objects.get(username=ret)
            print(user)
            loged = authenticate(username=ret.username, password=ret.password)
            if loged is not None:
                login(ret, loged)
                return render(request, 'user/account.html')
                print("log")
            else:
                print("notlog")
        return render(request, 'user/register.html', {'form_user' : form_user})
    form_user = UserCreationForm()
    return render(request, 'user/register.html', {'form_user' : form_user})

class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    lookup_field = 'username'

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), Is)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            MyUser.objects.create_user(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response({'status' : 'Bad request',
                         'message' : 'User could not be created with received data.'}, status=status.HTTP_400_BAD_REQUEST)


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
