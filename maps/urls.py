from django.urls import path
from . import views

urlpatterns = [
    path('france', views.france, name='france'),
    path('region/<int:region_id>', views.region, name='region'),
    path('department/<int:department_id>', views.department, name='department'),
    path('commune/<str:com>', views.commune, name='commune'),
    path('save/<str:title>', views.save, name='save'),
    path('del_favorite/<str:title>', views.del_favorite, name='del_favorite'),
]

app_name = 'maps'
