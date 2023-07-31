# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm, ListingForm


def bands_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/bands_list.html',
                  {'bands': bands})


def band_detail(request, id):  # notez le paramètre id supplémentaire
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request,
                  'listings/band_create.html',
                  {'form': form})


def band_update(request, id):
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_delete.html',
                  {'band': band})


def band_delete(request, id):
    band = Band.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('band-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'listings/band_delete.html',
                    {'band': band})

def about(request):
    return render(request,
                  'listings/about_us.html')


def redirect_email_sent(request):
    print('bonjour')
    return HttpResponse("<h1>EMAIL ENVOYE, NOUS VOUS REPONDRONS</h1>")


def contact(request):
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
             subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
             message=form.cleaned_data['message'],
             from_email=form.cleaned_data['email'],
             recipient_list=['admin@merchex.xyz'],
             )
        return redirect('email-sent')  # ajoutez cette instruction de retour
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()
    return render(request,
                  'listings/contact_us.html',
                  {'form': form})


def listing_list(request):
    listing = Listing.objects.all()
    return render(request,
                  'listings/listings_list.html',
                  {"listing": listing})


def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request,
                  'listings/listing_detail.html',
                  {"listing": listing})


def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            redirect('listing-detail', listing.id)
    else:
        form = ListingForm()
    return render(request,
                  'listings/listing_create.html',
                  {'form': form})


def listing_delete(request, id):
    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
        if Listing.objects.filter(id=id).exists():
            listing.delete()
        return redirect('listing-list')  # Redirection vers la liste des listes après la suppression

    return render(request,
                  'listings/listing_delete.html',
                  {'article': listing})
