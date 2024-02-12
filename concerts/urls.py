from django.urls import path
from .views import ConcertListCreateAPIView , ConcertDetailAPIView


urlpatterns = [
    path('', ConcertListCreateAPIView.as_view(), name='concert-list-create'),
    path('<int:pk>/', ConcertDetailAPIView.as_view(), name='Concert-detail'),
    ]


