from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.LoginFormView.as_view(
        template_name='login.html'), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile', views.profile, name='profile'),
    path('password_change', views.PasswordView.as_view(
        template_name='password.html',
        success_url='profile'),
         name='password_change'),
    path('del_user', views.del_user, name='del_user'),

]

app_name = 'users'
