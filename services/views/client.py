from django.shortcuts import render, get_object_or_404

from services.models import Service
from accounts.models import BarberProfile
from services.models.service import ServiceCategory
from services.utils import client_required, superadmin_blocked, barber_blocked


@superadmin_blocked
@barber_blocked
def home(request):
    return render(request, "client/home.html")


@superadmin_blocked
@barber_blocked
def about(request):
    return render(request, "client/about.html")


@superadmin_blocked
@barber_blocked
def barbers_list(request):
    barbers = BarberProfile.objects.all()
    return render(request, "client/barbers.html", {"barbers": barbers})


@superadmin_blocked
@barber_blocked
def barber_view(request, barber_id):
    barber = get_object_or_404(BarberProfile, id=barber_id)
    return render(request, "client/barber_view.html", {"barber": barber})


@superadmin_blocked
@barber_blocked
def categories_list(request):
    categories = ServiceCategory.objects.all()
    return render(request, "client/category/categories.html", {"categories": categories})


@superadmin_blocked
@barber_blocked
def category_view(request, category_id):
    category = get_object_or_404(ServiceCategory, id=category_id)
    return render(request, "client/category/category_view.html", {"category": category})


@client_required
def book(request):
    pass
