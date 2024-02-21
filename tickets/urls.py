from django.urls import path
from .views import TicketListCreateAPIView, TicketDestroyAPIView
from .views import UserLoginView

urlpatterns = [
    
    path('', TicketListCreateAPIView.as_view(), name='ticket-List-create'),
    path('<int:pk>/', TicketDestroyAPIView.as_view(), name='ticket-detail'),
    path('api/login/', UserLoginView.as_view(), name='user-login'),

]