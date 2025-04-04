from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
from django.db.models.aggregates import Sum, Avg
from django.shortcuts import redirect, render, get_object_or_404

from services.forms import HaircutEditForm, HaircutCreateForm, BarberEditForm, BarberCreateForm, UserEditForm, \
    CategoryCreateForm, CategoryEditForm, ServiceCreateForm, ServiceEditForm
from services.models import Service
from accounts.models import BarberProfile, CustomUser
from services.models.service import ServiceCategory
from services.utils import superadmin_required


@superadmin_required
def manage_barbers(request):
    barbers = BarberProfile.objects.all()
    return render(request, "admin/barbers/manage-barbers.html", {"barbers": barbers})


@superadmin_required
def manage_barber_view(request, barber_id):
    barber = BarberProfile.objects.get(id=barber_id)
    services = barber.services.all()
    return render(request, "services/../../templates/admin/barbers/barber_view.html",
                  {"barber": barber, "services": services})


@permission_required('services.add_barberprofile', raise_exception=True)
def barber_create(request):
    form = BarberCreateForm()
    if request.method == "POST":
        form = BarberCreateForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            # Adding to Barber Group
            barber_group = Group.objects.get(name="barber")
            user.groups.add(barber_group)

            return redirect("services:manage_barbers")

    return render(request, "services/../../templates/admin/barbers/barber_create.html", {"form": form})


@permission_required("services.change_barberprofile", raise_exception=True)
def barber_edit(request, barber_id):
    barber = BarberProfile.objects.get(id=barber_id)
    user = barber.user
    all_services = Service.objects.all()

    form = BarberEditForm(instance=barber, user_instance=user)
    # Pre-Fill the selected services
    form.fields['services'].initial = barber.services.all()

    if request.method == "POST":
        form = BarberEditForm(request.POST, request.FILES, instance=barber, user_instance=user)
        if form.is_valid():
            form.save()
            return redirect("services:manage_barbers")

    return render(request, "services/../../templates/admin/barbers/barber_edit.html",
                  {"form": form, "services": all_services})


@permission_required("services.delete_barberprofile", raise_exception=True)
def barber_delete(request, barber_id):
    barber = BarberProfile.objects.get(id=barber_id)
    barber.delete()

    user = barber.user

    # Group = Barber -> Client
    barber_group = Group.objects.get(name="barber")
    user.groups.remove(barber_group)

    client_group = Group.objects.get(name="client")
    user.groups.add(client_group)

    return redirect("services:manage_barbers")


# Main Page
@superadmin_required
def dashboard(request):
    # Getting Group members
    barbers = len(Group.objects.get(name="barber").user_set.all())
    clients = len(Group.objects.get(name="client").user_set.all())
    return render(request, "admin/general/dashboard.html", {"barbers": barbers, "clients": clients})


@superadmin_required
def users_list(request):
    users = CustomUser.objects.all().order_by('-is_active')
    return render(request, "admin/general/users_list.html", {"users": users})


@superadmin_required
def user_view(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, "admin/clients/user_view.html", {"user": user})


@superadmin_required
def user_edit(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    groups = Group.objects.all()

    form = UserEditForm(instance=user)
    form.fields['username'].widget.attrs['readonly'] = True

    if request.method == "POST":
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("services:users_list")

    return render(request, "admin/clients/user_edit.html", {"user": user, "groups": groups, "form": form})


@superadmin_required
def user_delete(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    return redirect("services:users_list")


@superadmin_required
def reports_list(request):
    return render(request, "admin/general/reports_list.html")


@superadmin_required
def settings(request):
    return render(request, "admin/general/settings.html")


@superadmin_required
def manage_clients(request):
    client_group = Group.objects.get(name="client")
    clients = CustomUser.objects.filter(groups=client_group)
    return render(request, "admin/clients/clients_list.html", {"clients": clients})


@superadmin_required
def client_view(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, "admin/clients/user_view.html", {"user": user})


@superadmin_required
def client_edit(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    groups = Group.objects.all()

    form = UserEditForm(instance=user)
    form.fields['username'].widget.attrs['readonly'] = True

    if request.method == "POST":
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("services:users_list")

    return render(request, "admin/clients/user_edit.html", {"user": user, "groups": groups, "form": form})


@superadmin_required
def client_delete(request, client_id):
    client = get_object_or_404(CustomUser, id=client_id)
    client.delete()
    return redirect("services:users_list")


@superadmin_required
def manage_appointments(request):
    pass


# TODO .
# TODO . Category Management
# TODO .

@superadmin_required
def manage_categories(request):
    categories = ServiceCategory.objects.all().order_by("-name")
    return render(request, "admin/services/categories/manage-categories.html",
                  {"categories": categories})


@superadmin_required
def manage_category_overview(request, category_id):
    category = ServiceCategory.objects.get(id=category_id)

    # Total
    total_services = category.services.count()
    total_price = category.services.aggregate(Sum("price"))["price__sum"] or 0
    total_duration = category.services.aggregate(Sum("duration"))["duration__sum"] or 0

    # Average
    average_duration = category.services.aggregate(Avg("duration"))["duration__avg"] or 0
    average_price = category.services.aggregate(Avg("price"))["price__avg"] or 0

    context = {
        "category": category,

        "total_services": total_services,
        "total_price": total_price,
        "total_duration": total_duration,

        "average_duration": average_duration,
        "average_price": average_price,
    }

    return render(request, "admin/services/categories/category-overview.html", {"context": context})


@superadmin_required
def manage_category_view(request, category_id):
    services = Service.objects.filter(category=category_id)
    category = ServiceCategory.objects.get(id=category_id)

    return render(request, "admin/services/categories/category_view.html", {"services": services, "category": category})


@superadmin_required
def category_create(request):
    form = CategoryCreateForm()

    if request.method == "POST":
        form = CategoryCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("services:manage_categories")

    return render(request, "admin/services/categories/category-create.html", {"form": form})


@superadmin_required
def category_edit(request, category_id):
    category = ServiceCategory.objects.get(id=category_id)

    form = CategoryEditForm(instance=category)
    if request.method == "POST":
        form = CategoryEditForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect("services:manage_categories")

    return render(request, "admin/services/categories/category-edit.html", {"category": category, "form": form})


@superadmin_required
def category_delete(request, category_id):
    category = ServiceCategory.objects.get(id=category_id)
    category.delete()
    return redirect("services:manage_categories")


# TODO . Service Management

@superadmin_required
def manage_services(request):
    return render(request, "admin/services/services/manage-services.html")


@superadmin_required
def manage_service_view(request, service_id):
    service = Service.objects.get(id=service_id)
    return render(request, "admin/services/services/service_view.html", {"service": service})


@superadmin_required
def service_create(request, category_id):
    category = ServiceCategory.objects.get(id=category_id)
    form = ServiceCreateForm()

    if request.method == "POST":
        form = ServiceCreateForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.category = category
            service.save()
            return redirect("services:manage_category_view", category_id=category_id)

    return render(request, "admin/services/services/service_create.html", {"form": form, "category": category})


@superadmin_required
def service_edit(request, service_id):
    service = Service.objects.get(id=service_id)
    category_id = service.category.id

    form = ServiceEditForm(instance=service)
    if request.method == "POST":
        form = ServiceEditForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect("services:manage_category_view", category_id)

    return render(request, "admin/services/services/service_edit.html", {"service": service, "form": form})


@superadmin_required
def service_delete(request, service_id):
    service = Service.objects.get(id=service_id)
    category_id = service.category.id
    service.delete()
    return redirect("services:manage_category_view", category_id=category_id)
