from rest_framework import serializers
from .models import Ticket
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 

        
class TicketSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Ticket
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        ticket = Ticket.objects.create(user=user, **validated_data)
        return ticket


class TicketQueryParamSerializer(serializers.Serializer):
    concert_id = serializers.IntegerField(required=False)
    person_id = serializers.IntegerField(required=False)
        