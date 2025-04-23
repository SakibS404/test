from django.shortcuts import render, redirect
from django.shortcuts import redirect
from .forms import RegisterForm






def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect ("signup_data/")
            
    else:
        form =RegisterForm()
    return  render(response,'register1/signup.html',{'form':form})




    
    
