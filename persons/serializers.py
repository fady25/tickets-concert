from rest_framework import serializers
from .models import Person
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'email','first_name'

class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Person
        fields = 'name','gender','age','user'
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        person = Person.objects.create(user=user, **validated_data)
        return person 

        