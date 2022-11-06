from django.contrib import admin
from flights.models import Flight, Booking

admin.site.register([Flight, Booking])