from rest_framework import generics
from .models import Concert
from .serializers import ConcertSerializer
from django.utils import timezone
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import UserLoginSerializer

class UserLoginView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer


class ConcertListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ConcertSerializer

    def get_queryset(self):
        current_datetime = timezone.now()
        concert = Concert.objects.filter(date__gte=current_datetime)
        return concert

    def get(self, request):
        return Response({'message': 'Authenticated user can access this view'})

class ConcertDetailAPIView(generics.RetrieveAPIView):
     queryset = Concert.objects.all()
     serializer_class = ConcertSerializer
    


    
