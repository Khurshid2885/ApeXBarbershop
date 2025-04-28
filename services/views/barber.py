from django.shortcuts import render

from services.utils import barber_required


@barber_required
def barber_dashboard(request):
    return render(request, "barber/general/dashboard.html")


@barber_required
def barber_schedule(request):
    return render(request, "barber/general/schedule.html")


@barber_required
def barber_appointments(request):
    return render(request, "barber/appointments/manage-appointments.html")


@barber_required
def barber_clients(request):
    return render(request, "barber/clients/clients.html")


@barber_required
def barber_services(request):
    return render(request, "barber/services/services_list.html")


# Profile / Settings
@barber_required
def barber_profile_view(request):
    return render(request, "barber/general/profile.html")


@barber_required
def barber_profile_edit(request):
    return render(request, "barber/general/profile-edit.html")


@barber_required
def barber_settings(request):
    return render(request, "barber/general/settings.html")
