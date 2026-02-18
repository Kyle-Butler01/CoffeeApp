from django.shortcuts import render, redirect



def home_page (request):
    return render (request, 'main/index.html')


def contacts_page (request):
    return render (request, 'main/contacts.html')


def cooperation_page (request):
    return render (request, 'main/cooperation.html')

