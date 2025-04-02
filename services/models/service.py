from django.core.validators import MinValueValidator, MaxValueValidator

from accounts.models import BarberProfile
from services.models.base import BaseModel
from django.db import models


class ServiceCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Service(BaseModel):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name="services", null=True,
                                 blank=True)
    barber = models.ManyToManyField(BarberProfile, related_name="services")
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3, validators=[
        MinValueValidator(0), MaxValueValidator(200.000)
    ])
    duration = models.PositiveIntegerField(default=30, help_text="minutes")
    img_file = models.ImageField(upload_to="services/%Y/%m/%d/")

    def __str__(self):
        return f"{self.name} ({self.category})"

    class Meta:
        ordering = ["-price"]
