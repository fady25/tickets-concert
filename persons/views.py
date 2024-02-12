from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer

   
class PersonListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PersonSerializer
   
    def get_queryset(self):
        concert_id = self.request.query_params.get('concert_id')
        persons = Person.objects.all ()
        
        if concert_id is not None:
            persons = Person.objects.filter(tickets__concert_id=concert_id)
        
        return persons 
    
   
class PersonDetailAPIView(generics.RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

