from rest_framework import generics
from .serializers import ProductSerializer
from products.models import Products



class ProductListViewAPI(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProductDetailViewAPI(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

