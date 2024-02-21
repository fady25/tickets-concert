from rest_framework import generics,permissions
from .models import Ticket
from .serializers import TicketSerializer, TicketQueryParamSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import UserLoginSerializer

class UserLoginView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

class TicketListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
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
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            return Response({"error": "User must be authenticated to create a ticket."}, status=401)
    
    def get(self, request):
        return Response({'message': 'Authenticated user can access this view'})




class TicketDestroyAPIView(generics.DestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

