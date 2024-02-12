from rest_framework import generics
from .models import Concert
from .serializers import ConcertSerializer
from django.utils import timezone

class ConcertListCreateAPIView(generics.ListCreateAPIView):
    #TODO filter out concerts that already passed  
    serializer_class = ConcertSerializer
    def get_queryset(self):
        current_datetime = timezone.now()
        queryset = Concert.objects.filter(date__gte=current_datetime)
        return queryset



class ConcertDetailAPIView(generics.RetrieveAPIView):
     queryset = Concert.objects.all()
     serializer_class = ConcertSerializer
    


    
