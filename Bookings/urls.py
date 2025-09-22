from django.urls  import path
from .views import RegisterView,LoginView,BusListCreateView,BusdetailView,BookingView,UserBookingView


urlpatterns=[
    path("register/",RegisterView.as_view(),name="register"),
    path("login/",LoginView.as_view(),name="login"),
    path("buses/",BusListCreateView.as_view(),name="buslist"),
    path("buses/<int:pk>/",BusdetailView.as_view()),
    path("booking/",BookingView.as_view(),name="bookings"),
    path("user/<int:user_id>/bookings/",UserBookingView.as_view(),name="user_bookings")
]