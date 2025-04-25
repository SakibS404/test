


from django.contrib import admin  # this block of code is to import the admin class
from .models import Person # this block of code is to import the  person model into the admin class


# this block of code is used to place the persons model within the admin page, holds all databases for this project
admin.site.register(Person)



















        
###############################################################################
#
# Reference:
#
# Simple UE is better then complex (2020). Extend User in Django part 2: Token Auth. 
#[online] YouTube. 
#Available at: https://www.youtube.com/watch?v=HDiMliULC18 [Accessed 25 Apr. 2025].
#
############################################################################
 
