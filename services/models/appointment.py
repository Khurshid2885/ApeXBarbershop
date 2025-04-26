from accounts.models import CustomUser, BarberProfile
from services.models.base import BaseModel, Status
from django.db import models

from services.models.service import Service


class Appointment(BaseModel):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="appointments")
    barber = models.ForeignKey(BarberProfile, on_delete=models.CASCADE, related_name="barber_appointments")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="services")
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10, choices=Status, default=Status.PENDING)
