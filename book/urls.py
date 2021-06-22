from django.conf.urls import url
from django.urls import path

from .views import BookingFlight

urlpatterns = [
    url(r'^book-flight/$', BookingFlight.post_flight, name='book flight'),
    url(r'^flights/$', BookingFlight.get_flight, name='get flights'),
    url(r'^flight-data/$', BookingFlight.get_flight_data, name='get flight data'),
    url(r'^update-flight/$', BookingFlight.update_flight, name='update flights'),
    url(r'^delete-flight/$', BookingFlight.delete_flight, name='delete flights'),
]