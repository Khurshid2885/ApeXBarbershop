from django.urls import path

from services.views import categories_list, barbers_list, barber_view, category_view, book_select_service, \
    book_select_barber

urlpatterns = [
    # Services
    # path('services/', services_list, name="services_list"),
    # path('service-view/<int:service_id>', service_view, name="service_view"),

    # Categories/Services
    path('categories/', categories_list, name="categories_list"),
    path('category-view/<int:category_id>', category_view, name="category_view"),

    # Barbers
    path('barbers/', barbers_list, name="barbers_list"),
    path('barber-view/<int:barber_id>', barber_view, name="barber_view"),

    # Book
    path('book/select-service/', book_select_service, name="book_select_service"),
    path('book/select-barber/', book_select_barber, name="book_select_barber"),
]
