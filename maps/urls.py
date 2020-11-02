from django.urls import path
from . import views

urlpatterns = [
    path('france', views.country, name='france'),
    path('region/<int:region_id>', views.region, name='region'),
]

app_name = 'maps'
