from django.urls import path

from services.views import haircuts_list, barbers_list, book, barber_view, haircut_view

urlpatterns = [
    # Services
    # path('services/', services_list, name="services_list"),
    # path('service-view/<int:service_id>', service_view, name="service_view"),

    # Haircuts
    path('haircuts/', haircuts_list, name="haircuts_list"),
    path('haircut-view/<int:haircut_id>', haircut_view, name="haircut_view"),

    # Barbers
    path('barbers/', barbers_list, name="barbers_list"),
    path('barber-view/<int:barber_id>', barber_view, name="barber_view"),

    # Book
    path('book/', book, name="book"),
]
