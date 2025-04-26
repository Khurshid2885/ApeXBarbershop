from services.models.appointment import Appointment
from services.models.base import BaseModel, Method, Status
from django.db import models


class Payment(BaseModel):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    method = models.CharField(max_length=10, choices=Method, default=Method.CASH)
    status = models.CharField(max_length=10, choices=Status, default=Status.PENDING)
    transaction_id = models.IntegerField(unique=True, blank=True, null=True)
