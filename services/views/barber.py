from django.db.models import Q
from django.shortcuts import render, redirect

from services.models import Appointment, Service
from services.utils import barber_required


# TODO -------------------------------------

# For better status visualization
def get_status_badge(status):
    return {
        'pending': 'warning',
        'confirmed': 'success',
        'completed': 'primary',
        'cancelled': 'danger',
    }.get(status, 'secondary')


# TODO -------------------------------------

@barber_required
def barber_dashboard(request):
    upcoming_appointments = Appointment.objects.filter(Q(barber=request.user.user_barber),
                                                       Q(status='pending')).order_by(
        "date")

    # Analytics Section
    total_revenue = 0
    completed_appointments = Appointment.objects.filter(status='completed').all()
    for appt in completed_appointments:
        total_revenue += appt.service.price

    total_appointments = len(Appointment.objects.filter(Q(barber__user=request.user), Q(status='completed')).all())
    total_services = len(Service.objects.filter(barber__user=request.user).all())

    for appt in upcoming_appointments:
        appt.status_badge = get_status_badge(appt.status)

    context = {
        "total_appointments": total_appointments,
        "total_services": total_services,
        "total_revenue": total_revenue,
        "upcoming_appointments": upcoming_appointments,
    }

    return render(request, "barber/general/dashboard.html", context)


@barber_required
def barber_schedule(request):
    return render(request, "barber/general/schedule.html")


# TODO .
# TODO . Appointments Management
# TODO .

@barber_required
def barber_appointments(request):
    appointments = Appointment.objects.filter(barber__user=request.user).order_by("date")

    # Filter by Date From
    date_from = request.GET.get('date_from')
    if date_from:
        appointments = appointments.filter(date__gte=date_from)

    # Filter By Date To
    date_to = request.GET.get('date_to')
    if date_to:
        appointments = appointments.filter(date__lte=date_to)

    # Filter by Status
    status = request.GET.get('status')
    if status:
        appointments = appointments.filter(status=status)

    # Add Status Badge
    for appt in appointments:
        appt.status_badge = get_status_badge(appt.status)

    return render(request, "barber/appointments/manage-appointments.html"
                  , {"appointments": appointments})


@barber_required
def barber_appointment_view(request, appt_id):
    appt = Appointment.objects.filter(id=appt_id)
    return render(request, "barber/appointments/appointment-view.html", {"appt": appt})


@barber_required
def barber_appointment_edit(request, appt_id):
    appt = Appointment.objects.filter(id=appt_id)
    return render(request, "barber/appointments/appointment-edit.html", {"appt": appt})


@barber_required
def barber_appointment_delete(request, appt_id):
    appt = Appointment.objects.filter(id=appt_id)
    appt.delete()
    return redirect("services:barber_appointments")


# TODO .
# TODO . Clients Management
# TODO .

@barber_required
def barber_clients(request):
    return render(request, "barber/clients/clients.html")


# TODO .
# TODO . Services Management
# TODO .

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
