from django.urls import path
from .views import PersonListCreateAPIView , PersonDetailAPIView 
from .views import UserLoginView

urlpatterns = [  
    
    path('', PersonListCreateAPIView.as_view(), name='Person-list-create'),
    path('<int:pk>/', PersonDetailAPIView.as_view(), name='Person-detail'),
    path('api/login/', UserLoginView.as_view(), name='user-login'),
]

