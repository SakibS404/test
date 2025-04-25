
#importing relevant extensions
from django.shortcuts import render, redirect
from django.shortcuts import redirect
from .forms import RegisterForm
from .models import Person





#creates a view function for register1 app, to handle http request and response 
def register(response):
    if response.method == 'POST':  #checks if it is a post method (submit)
        form = RegisterForm(response.POST)  #passes on submitted data through post 
        if form.is_valid():   #checks if form is valid
            
            user = form.save() #saves data in user model database

            Person.objects.create(     #creates a person in the person model database and saves the details listed below
                user=user,
                username=user.username,
                job_title = form.cleaned_data['job_title']

            
            )

        
        #redirects webpage after submission
        return redirect ("signup_data/")
            
            #if signup was invalid django forms points out the mistake made
    else:
        form =RegisterForm()
    return  render(response,'register1/signup.html',{'form':form})











        
###############################################################################
#
# Reference:
#
# Simple UE is better then complex (2020). Extend User in Django part 2: Token Auth. 
# [online] YouTube. 
# Available at: https://www.youtube.com/watch?v=HDiMliULC18 [Accessed 25 Apr. 2025].
#
#
#
# Tech With Tim (2019). Django Tutorial - User Registration & Sign Up Page. 
# [online] YouTube. 
# Available at: https://www.youtube.com/watch?v=Ev5xgwndmfc 
# [Accessed 20 Apr. 2025]
#
############################################################################
 
    
    
