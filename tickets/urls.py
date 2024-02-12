from django.urls import path
from .views import TicketCreateAPIView, TicketDestroyAPIView


urlpatterns = [
    
    path('', TicketCreateAPIView.as_view(), name='ticket-create'),
    path('<int:pk>/', TicketDestroyAPIView.as_view(), name='ticket-detail')

]