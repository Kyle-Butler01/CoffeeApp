from rest_framework import generics
from .serializers import ProductSerializer
from products.models import Products


#def APIinfo(request):
#    return render(request, 'api/api_info.html')


class ProductListViewAPI(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProductDetailViewAPI(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

