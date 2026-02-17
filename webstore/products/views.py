from django.shortcuts import render, get_object_or_404
from .models import Products
from django.contrib.auth.decorators import login_required


def ProductsView (request):
    products = Products.objects.all()
    return render (request, 'products/products_list.html', {'products':products})

@login_required
def ProductInfo (request, id):
    product = get_object_or_404(Products, id=id)
    return render (request, 'products/product_info.html', {'product': product})
