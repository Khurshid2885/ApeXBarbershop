from django.urls import path
from services.views import barbers_homepage

urlpatterns = [
    path('home/', barbers_homepage, name="barbers_homepage"),
]
