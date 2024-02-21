from rest_framework import serializers
from .models import Concert

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class ConcertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concert
        fields = 'name','date','location'

        