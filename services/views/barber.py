from django.db.models import Q, Count, Sum
from django.shortcuts import render, redirect, get_object_or_404

from accounts.forms import BarberProfileEditForm, BarberProfileImageForm
from accounts.models import BarberProfile, CustomUser
from services.forms import BarberAppointmentEditForm
from services.models import Appointment, Service
from services.models.service import ServiceCategory
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
    appt = get_object_or_404(Appointment, id=appt_id)

    appt.status_badge = get_status_badge(appt.status)
    return render(request, "barber/appointments/appointment-view.html", {"appointment": appt})


@barber_required
def barber_appointment_edit(request, appt_id):
    appt = get_object_or_404(Appointment, id=appt_id)
    form = BarberAppointmentEditForm(instance=appt)

    if request.method == 'POST':
        form = BarberAppointmentEditForm(data=request.POST, instance=appt)
        if form.is_valid():
            form.save()
            return redirect('services:barber_appointments')

    appt.status_badge = get_status_badge(appt.status)

    return render(request, "barber/appointments/appointment-edit.html", {"appointment": appt, "form": form})


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
    clients = CustomUser.objects.filter(appointments__barber__user=request.user).annotate(
        appointment_count=Count('appointments'))
    return render(request, "barber/clients/clients.html", {"clients": clients})


@barber_required
def barber_appointments_client(request, client_id):
    client = get_object_or_404(CustomUser, id=client_id)
    barber = request.user
    appointments = Appointment.objects.filter(client=client)

    context = {
        "client": client,
        "barber": barber,
        "appointments": appointments,
    }
    return render(request, "barber/clients/client-appointments.html", context)


# TODO .
# TODO . Services Management
# TODO .
@barber_required
def barber_categories(request):
    categories = ServiceCategory.objects.filter(category_services__barber__user=request.user).distinct()
    return render(request, "barber/services/categories/categories_list.html", {"categories": categories})


@barber_required
def barber_services(request, category_id):
    category = get_object_or_404(ServiceCategory, id=category_id)
    services = Service.objects.filter(category=category)
    return render(request, "barber/services/services/services_list.html", {"services": services, "category": category})


@barber_required
def barber_service_view(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, "barber/services/services/service-view.html", {"service": service})


# Profile / Settings
@barber_required
def barber_profile_view(request):
    return render(request, "barber/general/profile.html")


@barber_required
def barber_profile_edit(request):
    user = request.user
    barber = user.user_barber

    if request.method == "POST":
        user_form = BarberProfileEditForm(request.POST, instance=user)
        barber_form = BarberProfileImageForm(request.POST, request.FILES, instance=barber)
        if user_form.is_valid() and barber_form.is_valid():
            user_form.save()
            barber_form.save()
            return redirect("services:barber_profile_view")
    else:
        user_form = BarberProfileEditForm(instance=user)
        barber_form = BarberProfileImageForm(instance=barber)

    return render(request, "barber/general/profile-edit.html",
                  {"user_form": user_form, "barber_form": barber_form})


@barber_required
def barber_settings(request):
    return render(request, "barber/general/settings.html")
