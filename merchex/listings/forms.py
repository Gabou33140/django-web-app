# listings/forms.py

from django import forms
from listings.models import Band, Contact, Listing
    

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        # fields = '__all__'
        exclude = ('active', 'official_homepage')


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'