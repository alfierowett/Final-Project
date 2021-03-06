from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#Configuration of all paths to all installed apps on the project
urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'homepage/', include('home.urls')),
    path(r'memories/', include('memories.urls')),
    path(r'calendar/', include('calendarAlerts.urls')),
    path(r'documentWallet/', include('documentWallet.urls')),
    path(r'journal/', include('journal.urls')),
    path('accounts/', include('django.contrib.auth.urls')),


]
#Paths for static file storage of local DB
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)