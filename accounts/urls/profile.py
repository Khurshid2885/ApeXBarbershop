from django.urls import path

from accounts.views import settings_view, profile_view, profile_edit
from services.views import barber_profile_view, barber_profile_edit, barber_settings

urlpatterns = [
    # Client
    path("settings/", settings_view, name="settings_view"),
    path("profile/", profile_view, name="profile_view"),
    path("profile/edit/", profile_edit, name="profile_edit"),

]
