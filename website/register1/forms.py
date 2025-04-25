
#importing relavent extensions
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import JOB_TITLE_CHOICES  



#this creates the form for the signup page
class RegisterForm(UserCreationForm):

    
    
#this creates the drop down options for the job title 
    job_title_choices= [
        ('engineer','Engineer'),
        ('team_leader','Team Leader'),
        ('department_leader','Department Leader'),
        ('senior_manager','Senior Manager'),
        ('admin','Admin'),
        
        ]
    
    #this creates the different sign in details for the user to fill
     
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()
    job_title=forms.ChoiceField(choices=JOB_TITLE_CHOICES)
    
    



#this creates a model called user which stores the sign in details within the django database
    
    class Meta:
        model =User
        fields =['first_name','last_name','email','job_title','username','password1','password2']

    
#this is an extra process which isnt provided by django forms. It checks if a users email already exists within the database
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already taken")
        return email
    






###############################################################################
#Reference:
#Tech With Tim (2019). Django Tutorial - User Registration & Sign Up Page. 
#[online] YouTube. 
#Available at: https://www.youtube.com/watch?v=Ev5xgwndmfc 
#[Accessed 20 Apr. 2025]
#
############################################################################