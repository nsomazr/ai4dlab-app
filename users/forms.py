from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from .models import UserProfile
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
    password1 = forms.CharField(max_length=500, widget=(forms.PasswordInput(attrs={'class':'form-control','placeholder':'Type Password', 'id':'password'})))
    password2 = forms.CharField(max_length=500, widget=(forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-Type Password', 'id':'cpassword'})))

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

class ResetPasswordForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(required=True, max_length=100, widget=(forms.TextInput(attrs={'class':'form-control','placeholder':'Type Email', 'id':'email'})))

class ConfirmResetForm(SetPasswordForm):

    new_password1 = forms.CharField(max_length=200, widget=(forms.PasswordInput(attrs={'class':'form-control','placeholder':'Type New Password', 'id':'password1'})))
    new_password2 = forms.CharField(max_length=200, widget=(forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm New Password', 'id':'password2'})))


class StaffForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
    first_name = forms.CharField(required=True, max_length=30, widget=(forms.TextInput(attrs={'class':'form-control','placeholder':'First Name', 'id':'first_name'})))
    last_name = forms.CharField(required=True, max_length=30, widget=(forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name', 'id':'username'})))
    username = forms.CharField(required=True, max_length=30, widget=(forms.TextInput(attrs={'class':'form-control','placeholder':'Username', 'id':'username'})))
    email = forms.EmailField(required=True, max_length=100, widget=(forms.TextInput(attrs={'class':'form-control','placeholder':'Type Email', 'id':'email'})))
    role = forms.ChoiceField(
        choices=[('pi', 'PI'),('co_pi', 'CO-PI'),('ltc', 'Lab Training Coordinator'),
                 ('lo', 'Laison Officer'),('coordinator', 'Coordinator'),('asst_coordinator', 'Asst. Coordinator'),('researcher', 'Researcher'),
                 ('asst_researcher', 'Asst. Researcher'),('innovator', 'Innovator'),('student', 'Student')],
        widget=forms.Select(attrs={'class': 'form-control'})  
    )
    password1 = forms.CharField(max_length=500, widget=(forms.PasswordInput(attrs={'class':'form-control','placeholder':'Type Password', 'id':'password'})))
    password2 = forms.CharField(max_length=500, widget=(forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-Type Password', 'id':'cpassword'})))
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name','username', 'email','role', 'password1']
    
    def save(self, commit=True):
        user = super(StaffForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.role = self.cleaned_data['role']
        user.email = self.cleaned_data['email']
        user.is_staff = 1
        if commit:
            user.save()
        return user
