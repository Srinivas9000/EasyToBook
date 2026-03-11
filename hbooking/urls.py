"""
URL configuration for hbooking project.
"""
from django import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from trips import views as trip_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', trip_views.index_view, name='index'),
    path('', include('trips.urls')),
    path('accounts/', include('accounts.urls')),
    path('locations/', include('locations.urls')),
    path('bookings/', include('bookings.urls')),
    path('payments/', include('payments.urls')),
   

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
