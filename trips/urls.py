from django.urls import path
from . import views

app_name = 'trips'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('search/', views.trip_search_view, name='search'),
    path('trip/<int:pk>/', views.trip_detail_view, name='trip_detail'),
    path('contact/', views.contact, name='contact'),

]
