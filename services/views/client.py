from django.shortcuts import render, get_object_or_404

from accounts.models import BarberProfile
from services.models.service import ServiceCategory
from services.utils import client_required, superadmin_blocked, barber_blocked


@superadmin_blocked
@barber_blocked
def home(request):
    return render(request, "client/general/home.html")


@superadmin_blocked
@barber_blocked
def about(request):
    return render(request, "client/general/about.html")


@superadmin_blocked
@barber_blocked
def contact_us(request):
    return render(request, "client/general/contact-us.html")


@superadmin_blocked
@barber_blocked
def barbers_list(request):
    barbers = BarberProfile.objects.all()
    return render(request, "client/general/barbers.html", {"barbers": barbers})


@superadmin_blocked
@barber_blocked
def barber_view(request, barber_id):
    barber = get_object_or_404(BarberProfile, id=barber_id)
    return render(request, "client/book/barber_view.html", {"barber": barber})


@superadmin_blocked
@barber_blocked
def categories_list(request):
    categories = ServiceCategory.objects.all()
    return render(request, "client/category/categories.html", {"categories": categories})


@superadmin_blocked
@barber_blocked
def category_view(request, category_id):
    category = get_object_or_404(ServiceCategory, id=category_id)
    services = category.category_services.all()
    print(services)

    context = {
        "category": category,
        "services": services,
    }
    return render(request, "client/category/category_view.html", {"context": context})


@client_required
def book_select_service(request):
    return render(request, "client/book/book_selected_service.html")


@client_required
def book_select_barber(request):
    return render(request, "client/book/book_selected_service.html")
