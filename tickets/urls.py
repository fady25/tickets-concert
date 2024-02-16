from django.urls import path
from .views import TicketListCreateAPIView, TicketDestroyAPIView


urlpatterns = [
    
    path('', TicketListCreateAPIView.as_view(), name='ticket-List-create'),
    path('<int:pk>/', TicketDestroyAPIView.as_view(), name='ticket-detail')

]