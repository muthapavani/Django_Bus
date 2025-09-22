from rest_framework import serializers
from .models import Bus,Seat,Bookings
from django.contrib.auth.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["username","email","password"]

    def create(self,validate_data):
        user = User.objects.create_user(
            username=validate_data['username'],
            email=validate_data['email'],
            password=validate_data['password']
        )
        return user 
        
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seat
        fields=["id","seat_number","is_booked"]

class BusSerializer(serializers.ModelSerializer):
    Seats=SeatSerializer(many=True, read_only=True)
    class Meta:
        model= Bus
        fields="__all__"

class BookingSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer(read_only=True)
    bus = serializers.SerializerMethodField()
    seat = SeatSerializer(read_only=True)

    class Meta:
        model = Bookings
        fields = ['id', 'user', 'bus', 'seat', 'booking_time']

    def get_bus(self, obj):
        return {
            "id": obj.bus.id,
            "bus_name": obj.bus.bus_name,
            "origin": obj.bus.origin,
            "destination": obj.bus.destination,
            "start_time": obj.bus.start_time,
            "reach_time": obj.bus.reach_time
        }