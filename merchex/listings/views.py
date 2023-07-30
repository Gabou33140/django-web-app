# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing


def hello(request):
    bands = Band.objects.all()
    return render(request,
    'listings/hello.html',
    {'bands': bands})


def about(request):
    return render(request, 'listings/about_us.html')


def contact(request):
    return render(request, 'listings/contact_us.html')


def listing(request):
    listing = Listing.objects.all()
    return render(request, 'listings/listings.html', {"listing": listing})
