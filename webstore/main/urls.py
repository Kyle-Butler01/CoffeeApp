from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'main'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('products/', include('products.urls')),
    path('contacts/', views.contacts_page, name='contacts'),
    path('cooperation/', views.cooperation_page, name='cooperation'),
]


if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

