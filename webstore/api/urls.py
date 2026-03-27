from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api'

urlpatterns = [
    #path('api/', views.APIinfo, name='api-info'),
    path('v1/products/', views.ProductListViewAPI.as_view(), name='product-list-api'),
    path('v1/products/<int:pk>/', views.ProductDetailViewAPI.as_view(), name='product-detail-api'),
    path('v1/login/', obtain_auth_token, name='api-login'),
]