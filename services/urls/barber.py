from django.urls import path
from services.views import barber_dashboard, barber_schedule, barber_appointments, \
    barber_clients, barber_services, \
    barber_settings, barber_profile_view, barber_profile_edit, barber_appointment_edit, barber_appointment_view, \
    barber_appointment_delete, barber_appointments_client, barber_service_view, barber_categories, barber_service_delete

urlpatterns = [
    # Main - Navbar
    path("dashboard/", barber_dashboard, name="barber_dashboard"),
    path("schedule/", barber_schedule, name="barber_schedule"),
    path("appointments/", barber_appointments, name="barber_appointments"),
    path("clients/", barber_clients, name="barber_clients"),
    path("categories/", barber_categories, name="barber_categories"),

    # Barber - Right Side of Navbar
    path("profile/", barber_profile_view, name="barber_profile_view"),
    path("profile/edit", barber_profile_edit, name="barber_profile_edit"),
    path("settings/", barber_settings, name="barber_settings"),

    # Client
    path("clients/<int:client_id>/appointments/", barber_appointments_client, name="barber_appointments_client"),

    # Appointments
    path("appointments/<int:appt_id>", barber_appointment_view, name="barber_appointment_view"),
    path("appointments/<int:appt_id>/edit", barber_appointment_edit, name="barber_appointment_edit"),
    path("appointments/<int:appt_id>/delete", barber_appointment_delete, name="barber_appointment_delete"),

    # Services/Categories
    path("categories/<int:category_id>", barber_services, name="barber_services"),
    path("services/<int:service_id>", barber_service_view, name="barber_service_view"),
    path("services/<int:service_id>/delete", barber_service_delete, name="barber_service_delete"),
]
