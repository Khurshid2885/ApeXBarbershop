from django.shortcuts import render

from services.models import Service
from accounts.models import BarberProfile
from services.utils import client_required

@client_required
def home(request):
    return render(request, "services/home.html")

@client_required
def about(request):
    return render(request, "services/about.html")

@client_required
def barbers_list(request):
    barbers = BarberProfile.objects.all()
    return render(request, "services/barbers.html", {"barbers": barbers})

@client_required
def haircuts_list(request):
    haircuts = Service.objects.all()
    return render(request, "services/haircuts.html", {"haircuts": haircuts})

@client_required
def book(request):
    pass
