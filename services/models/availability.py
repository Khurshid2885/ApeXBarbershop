from django.db import models

from accounts.models import BarberProfile
from services.models.base import BaseModel


class Availability(BaseModel):
    barber = models.ForeignKey(BarberProfile, on_delete=models.CASCADE, related_name="availability")
    date = models.DateField()
    time = models.TimeField()
