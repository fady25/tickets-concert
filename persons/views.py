from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import UserLoginSerializer


class UserLoginView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

   
class PersonListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PersonSerializer
    def get_queryset(self):
        concert = self.request.query_params.get('concert')
        persons = Person.objects.all ()
        
        if concert:
            persons = Person.objects.filter(tickets__concert_id=concert)
        
        return persons 
    
    def get(self, request):
        return Response({'message': 'Authenticated user can access this view'})
    
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            return Response({"error": "User must be authenticated to create a person."}, status=401)
        
class PersonDetailAPIView(generics.RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

