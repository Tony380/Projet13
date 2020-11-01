from django.urls import path
from . import views

urlpatterns = [
    path('country', views.country, name='country'),
    path('region/<int:region_id>', views.region, name='region'),
]

app_name = 'maps'
