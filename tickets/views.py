from rest_framework import generics,permissions
from .models import Ticket
from .serializers import TicketSerializer, TicketQueryParamSerializer



class TicketListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        query_param_serializer = TicketQueryParamSerializer(data=self.request.query_params)
        query_param_serializer.is_valid(raise_exception=True)

        concert = query_param_serializer.validated_data.get("concert")
        person = query_param_serializer.validated_data.get("person")

        tickets = Ticket.objects.all()

        if concert:
            tickets = tickets.filter(concert=concert)

        if person:
            tickets = tickets.filter(person=person)
        
        return tickets
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class TicketDestroyAPIView(generics.DestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

