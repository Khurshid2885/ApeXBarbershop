from django.urls import path
from services.views import barber_dashboard, barber_schedule, barber_appointments, barber_clients, barber_services, \
    barber_profile, barber_settings

urlpatterns = [
    # Main - Navbar
    path("dashboard/", barber_dashboard, name="barber_dashboard"),
    path("schedule/", barber_schedule, name="barber_schedule"),
    path("appointments/", barber_appointments, name="barber_appointments"),
    path("clients/", barber_clients, name="barber_clients"),
    path("services/", barber_services, name="barber_services"),

    # Right Side
    path("profile/", barber_profile, name="barber_profile"),
    path("settings/", barber_settings, name="barber_settings"),
]
