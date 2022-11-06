from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from flights.serializers import FlightListSerializer, BookingListSerializer
from django.utils import timezone

class FlightListView(ListAPIView):
    queryset = Flight.objects.all() #Gonna fetch all of flight instances
    serializer_class = FlightListSerializer
    
class UpcomingBookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gt=timezone.now())
    serializer_class = BookingListSerializer
    
class BookingListView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer
    
    #Both UpcomingBookingListView AND BookingListView are using the same serializer