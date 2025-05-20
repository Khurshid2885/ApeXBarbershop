from django.urls.conf import path, include
from services.views import home, about, contact_us

app_name = "services"

urlpatterns = [
    path('', home, name="home"),  # Home route
    path('about/', about, name="about"),  # About route
    path('contact-us/', contact_us, name="contact_us"),  # About route

    # Admin
    path('services/admin/', include('services.urls.admin')),

    # Barber
    path('services/barber', include('services.urls.barber')),

    # Client
    path('services/', include('services.urls.client')),

]
