from django.contrib import admin

from accounts.models import CustomUser, BarberProfile
from .models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(BarberProfile)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(Review)
admin.site.register(Availability)
admin.site.register(Payment)
