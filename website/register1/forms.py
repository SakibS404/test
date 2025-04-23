from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(UserCreationForm):

    
    

    job_title_choices= [
        ('engineer','Engineer'),
        ('team_leader','Team Leader'),
        ('department_leader','Department Leader'),
        ('senior_manager','Senior Manager'),
        ('admin','Admin'),
        
        ]
     
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()
    job_title=forms.ChoiceField(choices=job_title_choices)
    
    


    
    class Meta:
        model =User
        fields =['first_name','last_name','email','job_title','username','password1','password2']

    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already taken")
        return email