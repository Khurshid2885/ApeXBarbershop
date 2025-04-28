from django.urls import path
from services.views import barber_dashboard, barber_schedule, barber_appointments, \
    barber_clients, barber_services, \
    barber_settings, barber_profile_view, barber_profile_edit

urlpatterns = [
    # Main - Navbar
    path("dashboard/", barber_dashboard, name="barber_dashboard"),
    path("schedule/", barber_schedule, name="barber_schedule"),
    path("appointments/", barber_appointments, name="barber_appointments"),
    path("clients/", barber_clients, name="barber_clients"),
    path("services/", barber_services, name="barber_services"),

    # Barber - Right Side of Navbar
    path("profile/", barber_profile_view, name="barber_profile_view"),
    path("profile/edit", barber_profile_edit, name="barber_profile_edit"),
    path("settings/", barber_settings, name="barber_settings"),
]
