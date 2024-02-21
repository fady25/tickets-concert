from rest_framework import serializers
from .models import Ticket

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = 'seat_number','gate_number','user'

    
class TicketQueryParamSerializer(serializers.Serializer):
    concert_id = serializers.IntegerField(required=False)
    person_id = serializers.IntegerField(required=False)
        