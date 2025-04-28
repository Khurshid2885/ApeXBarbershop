from django.urls import path

from services.views.admin import admin_dashboard, manage_barbers, manage_clients, manage_categories, \
    manage_appointments, \
    users_list, reports_list, settings, user_edit, user_delete, user_view, manage_barber_view, barber_create, \
    barber_edit, admin_profile_view, admin_profile_edit, \
    barber_delete, client_view, \
    client_edit, client_delete, \
    manage_service_view, category_edit, \
    manage_category_view, category_create, category_delete, service_create, service_edit, \
    service_delete, manage_category_overview, appointment_view, appointment_create, appointment_edit, appointment_delete

urlpatterns = [
    # Main - Navbar
    path("dashboard/", admin_dashboard, name="admin_dashboard"),
    path("users/", users_list, name="users_list"),
    path("reports/", reports_list, name="reports_list"),
    path("settings/", settings, name="settings"),

    # Profile
    path("profile/", admin_profile_view, name="admin_profile_view"),
    path("profile/edit", admin_profile_edit, name="admin_profile_edit"),

    # Management
    path("manage-barbers/", manage_barbers, name="manage_barbers"),
    path("manage-clients/", manage_clients, name="manage_clients"),
    path("manage-appointments/", manage_appointments, name="manage_appointments"),
    path("manage-categories/", manage_categories, name="manage_categories"),

    # Appointments
    path("appointment-view/", appointment_view, name="appointment_view"),
    path("appointment-create/", appointment_create, name="appointment_create"),
    path("appointment-edit/", appointment_edit, name="appointment_edit"),
    path("appointment-delete/", appointment_delete, name="appointment_delete"),

    # Users
    path("user-view/<int:user_id>", user_view, name="user_view"),
    path("user-edit/<int:user_id>", user_edit, name="user_edit"),
    path("user-delete/<int:user_id>", user_delete, name="user_delete"),

    # Barbers
    path('barber-create/', barber_create, name="manage_barber_create"),
    path('barber-view/<int:barber_id>', manage_barber_view, name="manage_barber_view"),
    path('barber-edit/<int:barber_id>', barber_edit, name="manage_barber_edit"),
    path('barber-delete/<int:barber_id>', barber_delete, name="manage_barber_delete"),

    # Clients
    path("services-view/<int:client_id>", client_view, name="client_view"),
    path("services-edit/<int:client_id>", client_edit, name="client_edit"),
    path("services-delete/<int:client_id>", client_delete, name="client_delete"),

    # Categories
    path("category-overview/<int:category_id>/", manage_category_overview, name="manage_category_overview"),
    path("category-view/<int:category_id>/", manage_category_view, name="manage_category_view"),
    path("category-create/", category_create, name="category_create"),
    path("category-edit/<int:category_id>/", category_edit, name="category_edit"),
    path("category-delete/<int:category_id>/", category_delete, name="category_delete"),

    # Category --> Services
    path("service-view/<int:service_id>/", manage_service_view, name="manage_service_view"),
    path("service-create/<int:category_id>/", service_create, name="service_create"),
    path("service-edit/<int:service_id>/", service_edit, name="service_edit"),
    path("service-delete/<int:service_id>/", service_delete, name="service_delete"),
]
