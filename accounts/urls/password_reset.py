from django.urls import path

from accounts.views import forget_password, verify_code, reset_password

urlpatterns = [
    path("forget_password/", forget_password, name="forget_password"),
    path("verify_code/", verify_code, name="verify_code"),
    path("reset_password/", reset_password, name="reset_password"),
]
