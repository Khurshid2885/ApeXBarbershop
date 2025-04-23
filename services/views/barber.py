from django.shortcuts import render


def barbers_homepage(request):
    return render(request, "barber/home.html")
