
from django.contrib import admin
from django.urls import path, include
from register1 import views as views1



urlpatterns = [
    path('signup_data/', admin.site.urls),
    
    path('signup/',views1.register,name='signup'),

  

]
