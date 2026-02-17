from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'products'
 

urlpatterns = [
    path('', views.ProductsView, name='productslist' ),
    path('product/<int:id>/', views.ProductInfo, name='productinfo'),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )