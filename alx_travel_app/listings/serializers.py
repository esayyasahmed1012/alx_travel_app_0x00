# listings/serializers.py
from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    host = serializers.ReadOnlyField(source='host.username')

    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'location', 'price_per_night', 'host', 'created_at', 'updated_at', 'is_available']

class BookingSerializer(serializers.ModelSerializer):
    guest = serializers.ReadOnlyField(source='guest.username')

    class Meta:
        model = Booking
        fields = ['id', 'listing', 'guest', 'check_in', 'check_out', 'total_price', 'status', 'created_at']
