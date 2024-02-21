from django.urls import path
from .views import ConcertListCreateAPIView , ConcertDetailAPIView
from .views import UserLoginView


urlpatterns = [
    path('', ConcertListCreateAPIView.as_view(), name='concert-list-create'),
    path('<int:pk>/', ConcertDetailAPIView.as_view(), name='Concert-detail'),
    path('api/login/', UserLoginView.as_view(), name='user-login'),
    
    ]


