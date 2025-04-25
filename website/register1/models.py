#importing relevant extensions
from django.db import models
from django.contrib.auth.models import User



#this code declares the job title drop down options which will be stored in the Persons model database
JOB_TITLE_CHOICES = [
    ('engineer', 'Engineer'),
    ('team_leader', 'Team Leader'),
    ('department_leader', 'Department Leader'),
    ('senior_manager', 'Senior Manager'),
    ('admin', 'Admin'),
]

#creating a persons model. This is to store the job titles within the database as it is not provided by django in the  user model
class Person(models.Model):

    # creating a one to one relationship between user model and persons model (making them interconnected)
    user =models.OneToOneField(User,on_delete=models.CASCADE,related_name='person')

    username =models.CharField(max_length=200)
    
    job_title=models.CharField(max_length=200,choices=JOB_TITLE_CHOICES)










###############################################################################
#Reference:
#Tech With Tim (2019). Django Tutorial - User Registration & Sign Up Page. 
#[online] YouTube. 
#Available at: https://www.youtube.com/watch?v=Ev5xgwndmfc 
#[Accessed 20 Apr. 2025]
#
############################################################################
 

