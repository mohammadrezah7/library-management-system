from django import forms
from .models import reservations

class contactForm2(forms.ModelForm):
    class Meta:
        model = reservations
        fields = '__all__'