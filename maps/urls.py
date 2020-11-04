from django.urls import path
from . import views

urlpatterns = [
    path('france', views.france, name='france'),
    path('region/<int:region_id>', views.region, name='region'),
]

app_name = 'maps'
