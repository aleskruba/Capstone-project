# restaurant/views.py
from rest_framework import generics, viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer,BookingSerializer

# View for listing all menu items and creating a new menu item
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# View for retrieving, updating, and deleting a single menu item
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer