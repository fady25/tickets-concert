from rest_framework import serializers
from .models import Ticket


        
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

    
class TicketQueryParamSerializer(serializers.Serializer):
    concert_id = serializers.IntegerField(required=False)
    person_id = serializers.IntegerField(required=False)
        