from rest_framework import serializers
from .models import Concert

class ConcertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concert
        fields = 'name','date','location'

        