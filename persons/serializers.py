from rest_framework import serializers
from .models import Person
from django.contrib.auth.models import User

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'email','first_name'

class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Person
        fields = 'name','gender','age','user'
    
    

        