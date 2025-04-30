from django.db import models

from accounts.models import CustomUser, BarberProfile
from services.models.base import BaseModel


class Review(BaseModel):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="customer_review")
    barber = models.ForeignKey(BarberProfile, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'review'
