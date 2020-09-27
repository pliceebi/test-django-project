from django.contrib.auth import views as auth_views
from django.urls import path

from . import views as user_views

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('success_registration/', user_views.success_registration, name='success-registration'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('success_login/', user_views.success_login, name='success-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
