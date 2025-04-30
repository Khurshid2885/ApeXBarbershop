from django.contrib.auth.models import AbstractUser
from django.db import models
from common.models import Base


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    profile_photo = models.ImageField(upload_to="accounts/", blank=True, null=True, default="accounts/profile.png")
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        db_table = 'customuser'

class Code(Base):
    code = models.CharField(max_length=4)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_code", null=True, blank=True)

    class Meta:
        db_table = 'code'