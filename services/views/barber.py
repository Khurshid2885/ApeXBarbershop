from django.shortcuts import render


def barber_dashboard(request):
    return render(request, "barber/general/dashboard.html")


def barber_schedule(request):
    return render(request, "barber/general/schedule.html")


def barber_appointments(request):
    return render(request, "barber/appointments/manage-appointments.html")


def barber_clients(request):
    return render(request, "barber/clients/clients.html")


def barber_services(request):
    return render(request, "barber/services/services_list.html")


# Profile / Settings
def barber_profile(request):
    return render(request, "barber/general/profile.html")


def barber_settings(request):
    return render(request, "barber/general/settings.html")
