# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
# from django.shortcuts import render
from listings.models import Band, Listing


def hello(request):
    band = Band.objects.all()
    return HttpResponse(f"""
            <h1>Hello Django!</h1>
            <p> Voici 3 groupes : <p>
            <ul>
                <li>{band[0]}</li>
                <li>{band[1]}</li>
                <li>{band[2]}</li>
            </ul>
            """)


def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')


def contact(request):
    return HttpResponse('<h1>Contacte nous:</h1>')


def listing(request):
    listing = Listing.objects.all()
    return HttpResponse(f"""
            <h1>Voici la liste:</h1>
            <ul>
                <li>{listing[0]}</li>
                <li>{listing[1]}</li>
                <li>{listing[2]}</li>
            </ul>
            """)
