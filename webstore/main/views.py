from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page


def home_page (request):
    return render (request, 'main/index.html')


@cache_page(60, key_prefix='contacts')
def contacts_page (request):
    return render (request, 'main/contacts.html')


@cache_page(60, key_prefix='cooperation')
def cooperation_page (request):
    return render (request, 'main/cooperation.html')

