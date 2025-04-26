from django.urls import path, include

app_name = "accounts"

urlpatterns = [
    path('', include('accounts.urls.auth')),
    path('profile/', include('accounts.urls.profile')),
    path('password/', include('accounts.urls.password_reset')),
]
