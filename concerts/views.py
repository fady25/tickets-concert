from rest_framework import generics
from .models import Concert
from .serializers import ConcertSerializer
from django.utils import timezone

class ConcertListCreateAPIView(generics.ListCreateAPIView):
 
    serializer_class = ConcertSerializer
    def get_queryset(self):
        current_datetime = timezone.now()
        concert = Concert.objects.filter(date__gte=current_datetime)
        return concert



class ConcertDetailAPIView(generics.RetrieveAPIView):
     queryset = Concert.objects.all()
     serializer_class = ConcertSerializer
    


    
