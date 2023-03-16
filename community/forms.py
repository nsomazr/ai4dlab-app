from django import forms
from django.utils import timezone
from .models import UDOMAI

col =(
    (1, "College of Business and Economics"),
    (2, "College of Earth Sciences and Engineering"),
    (3, "College of Education"),
    (4, "College of Humanities and Social Sciences"),
    (5, "College of Informatics and Virtual Education"),
    (6, "College of Natural and Mathematical Sciences"),
    (7, "School of Law"),
    (8, "School of Medicine and Dentistry"),
    (9, "School of Nursing and Public Health"),
    (10, "Confucius Institute"),
    (11, "Institute of Development Studies")
)




yo =(
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

class UDOMAIForm(forms.ModelForm):
    first_name  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'first-name', 'placeholder':'First Name'})))
    last_name  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'first-name', 'placeholder':'Last Name'})))
    college = forms.ChoiceField(choices=col, widget=(forms.Select(attrs={'class': 'form-control', 'id':'college', 'placeholder':'Choose College'})))
    yos = forms.ChoiceField(choices=yo, widget=(forms.Select(attrs={'class': 'form-control', 'id':'college', 'placeholder':'Choose Year of Study'})))
    programme  = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'id':'first-name', 'placeholder':'Programme'})))
    phone  = forms.IntegerField(widget=(forms.NumberInput(attrs={'class': 'form-control', 'id':'phone-number', 'placeholder':'Phone Number'})))
    email  = forms.EmailField(max_length=100, widget=(forms.EmailInput(attrs={'class': 'form-control', 'id':'email', 'placeholder':'Email Address'})))

    
    class Meta:
        model = UDOMAI
        fields = ['first_name', 'last_name', 'college','yos','email','phone']


    