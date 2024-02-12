from django.urls import path
from .views import PersonListCreateAPIView , PersonDetailAPIView 


urlpatterns = [  
    
    path('', PersonListCreateAPIView.as_view(), name='Person-list-create'),
    path('<int:pk>/', PersonDetailAPIView.as_view(), name='Person-detail')
]

