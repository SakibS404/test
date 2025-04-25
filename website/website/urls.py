#import relevant extensions
from django.contrib import admin
from django.urls import path, include
from register1 import views as views1


#creates the url path to each webpage
urlpatterns = [
    path('database/', admin.site.urls),
    
    path('signup/',views1.register,name='signup'),

  

]

















###############################################################################
#Reference:
#Tech With Tim (2019). Django Tutorial - User Registration & Sign Up Page. 
#[online] YouTube. 
#Available at: https://www.youtube.com/watch?v=Ev5xgwndmfc 
#[Accessed 20 Apr. 2025]
#
############################################################################
