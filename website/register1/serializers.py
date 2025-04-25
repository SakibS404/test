#code to import relevant extensions

from rest_framework import serializers
from .models import Person
from django.contrib.auth.models import User


#creating a serialiser of the persons model allowing it to interact with django API
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'  #specifies that all fields of the person model should be included

#nesting user model serialiser inside person serialiser
class UserSerializer(serializers.ModelSerializer):
    person=PersonSerializer()

    #tells django which model and fields to be included in the nested serialiser
    class Meta:
        model=User
        fields=['username','email','person']













        
###############################################################################
#
# Reference:
#
# Simple UE is better then complex (2020). Extend User in Django part 2: Token Auth. 
#[online] YouTube. 
#Available at: https://www.youtube.com/watch?v=HDiMliULC18 [Accessed 25 Apr. 2025].
#
############################################################################
 
        

    