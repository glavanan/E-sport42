from django import forms
from base.models import MyUser
from django_countries.fields import CountryField
from django.contrib.admin import widgets
from datetime import datetime

class UserCreationForm(forms.ModelForm):
    """
    Form to creat user, it's overide UserCreationForm because our overwrite of User
    we want Username, fist/last name, password, check password, email, and birthdate
    """
    error_messages = {
        'duplicate_username': ("Username deja utilise / Username already used."),
        'password_mismatch': ("les mots de pass ne sont pas identique / the tow password field didn't match"),
        }
    username = forms.CharField(label = ("Username"), max_length=30, help_text=("Requis: 30 character ou moins"), error_messages={'invalid':("invalide username")})
    password1 = forms.CharField(label= ("Password"), max_length=255, widget = forms.PasswordInput)
    password2 = forms.CharField(label=("Password confirmation"), max_length=255, widget=forms.PasswordInput, help_text=("entrer le meme password que precedent."))
    fisrt_name = forms.CharField(label=("Prenom"), max_length=40)
    last_name = forms.CharField(label=("Nom"), max_length=40)
    email = forms.EmailField(label=("Email"), max_length=255)
    address = forms.CharField(label=("adresse"), widget =forms.Textarea)
    nationality = CountryField()
    birth_date = forms.DateField(label=("Date de naissance (format : DD/MM/AAAA)"), widget=forms.widgets.DateInput(format="%d/%m/%Y"))
    phone = forms.CharField(label=("Telephone (Optionnel)"), max_length = 14, required=False)

    class Meta:
        model = MyUser
        fields = ("username", "password1", "password2", "email", "address", "nationality", "birth_date", "phone")
