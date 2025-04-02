from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.i18n import set_language

from config import settings

urlpatterns = i18n_patterns(
    # Admin
    path('admin/', admin.site.urls),

    # Home, About
    path('', include('services.urls')),

    # Services
    path('services/', include('services.urls')),

    # Accounts
    path('accounts/', include('accounts.urls')),

    # Rosetta - Internationalization
    path('rosetta/', include('rosetta.urls')),

    # Change language button access url
    path('i18n/setlang/', set_language, name='set_language')
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
