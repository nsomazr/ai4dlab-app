from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django_countries.data import COUNTRIES

from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(max_length=200, widget=(forms.TextInput(attrs={'class':'form-control','placeholder':'Type Username', 'id':'username'})))
    password = forms.CharField(max_length=200, widget=(forms.PasswordInput(attrs={'class':'form-control','placeholder':'Type Password', 'id':'password'})))


class NewUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
    
    first_name = forms.CharField(required=True, max_length=30, widget=(forms.TextInput(attrs={'class':'form-control','placeholder':'Type firstname', 'id':'first-name'})))
    last_name = forms.CharField(required=True, max_length=30, widget=(forms.TextInput(attrs={'class':'form-control','placeholder':'Type last name', 'id':'last-name'})))
    username = forms.CharField(required=True, max_length=30, widget=(forms.TextInput(attrs={'class':'form-control','placeholder':'Username', 'id':'username'})))
    company = forms.CharField(required=True, max_length=30, widget=(forms.TextInput(attrs={'class':'form-control','placeholder':'Company/Institution', 'id':'company'})))
    email = forms.EmailField(required=True, max_length=100, widget=(forms.TextInput(attrs={'class':'form-control','placeholder':'Type Email', 'id':'email'})))
    country = forms.ChoiceField(choices=sorted(COUNTRIES.items()), widget=(forms.Select(attrs={'class':'form-control','placeholder':'Select Country', 'id':'country'})))
    password1 = forms.CharField(max_length=200, widget=(forms.PasswordInput(attrs={'class':'form-control','placeholder':'Type Password', 'id':'password'})))
    password2 = forms.CharField(max_length=200, widget=(forms.PasswordInput(attrs={'class':'form-control','placeholder':'Type Password', 'id':'cpassword'})))

    class Meta:

        model = User

        fields = ('first_name', 'last_name', 'username', 'company', 'country', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.company = self.cleaned_data['company']
        user.country = self.cleaned_data['country']
        if commit:
            user.save()
        return user