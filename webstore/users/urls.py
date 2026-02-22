from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'users'

urlpatterns = [
    path('registration/', views.register_page, name='register'),
    path('login/', LoginView.as_view(template_name = 'users/login.html'), name= 'login'),
    path('logout/', LogoutView.as_view(next_page = 'main:home'), name='logout'),
    path('profile/', views.profile_page, name='profile'),
    path('profile/edit/', views.edit_profile_page, name='edit_profile'),
]