from django.urls import path
from . import views

urlpatterns = [
    path('france', views.france, name='france'),
    path('region/<int:region_id>', views.region, name='region'),
    path('department/<int:department_id>', views.department, name='department'),
    path('commune/<str:com>', views.commune, name='commune'),
]

app_name = 'maps'
