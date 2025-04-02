from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from accounts.models.base import BaseModel
from accounts.models.user import CustomUser


class BarberProfile(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="user_barber")
    bio = models.TextField(null=True, blank=True)
    experience_years = models.PositiveIntegerField(default=0, help_text="Years of experience")
    image = models.ImageField(upload_to="barbers/", null=True, blank=True, default="barbers/default-barber.png")
    rating = models.DecimalField(default=3.0, decimal_places=1, max_digits=2, validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = "-rating",
