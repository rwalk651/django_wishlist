from django import forms
from .models import Place

class NewPlaceForm(forms.ModelForm):

    # https://docs.djangoproject.com/en/dev/topics/db/models/#meta-options
    # https://docs.djangoproject.com/en/dev/ref/models/options/
    class Meta:
        model = Place
        fields = ('name', 'visited')