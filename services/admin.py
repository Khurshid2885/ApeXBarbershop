from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from accounts.models import CustomUser, BarberProfile
from .models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(BarberProfile)
admin.site.register(Appointment)
admin.site.register(Review)
admin.site.register(Availability)
admin.site.register(Payment)
admin.site.register(Service)


class ServiceAdmin(TranslationAdmin):
    list_display = ('name',)
