from django.contrib import admin
from .models import Bus,Seat,Bookings
# Register your models here.
class BusAdmin(admin.ModelAdmin):
    list_display=("bus_name","number","origin","destination","features","start_time","reach_time","price","no_of_seats")
admin.site.register(Bus,BusAdmin)

class SeatAdmin(admin.ModelAdmin):
    list_display=("id","bus","seat_number","is_booked")
admin.site.register(Seat,SeatAdmin)

class BookingsAdmin(admin.ModelAdmin):
    list_display=("user","bus","seat","booking_time")
admin.site.register(Bookings,BookingsAdmin)