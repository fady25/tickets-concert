from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer

   
class PersonListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PersonSerializer
   
    def get_queryset(self):
        concert = self.request.query_params.get('concert')
        persons = Person.objects.all ()
        
        if concert:
            persons = Person.objects.filter(tickets__concert_id=concert)
        
        return persons 
    
   
class PersonDetailAPIView(generics.RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

