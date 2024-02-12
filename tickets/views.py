from rest_framework import generics
from .models import Ticket
from .serializers import TicketSerializer, TicketQueryParamSerializer
from rest_framework.response import Response
from rest_framework import status




class TicketCreateAPIView(generics.CreateAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        query_param_serializer = TicketQueryParamSerializer(data=self.request.query_params)
        query_param_serializer.is_valid(raise_exception=True)

        concert_id = query_param_serializer.validated_data.get("concert_id")
        person_id = query_param_serializer.validated_data.get("person_id")

        tickets = Ticket.objects.all()

        if concert_id:
            tickets = tickets.filter(concert=concert_id)

        if person_id:
            tickets = tickets.filter(person=person_id)
        
        return tickets
    
    
    

class TicketListAPIView(generics.ListAPIView):
    serializer_class = TicketSerializer
    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)
    
class TicketDestroyAPIView(generics.DestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

