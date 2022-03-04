from .models import Wish
from django.forms import ModelForm, DateInput
from django import forms
from django.core.validators import MinValueValidator

class WishForm(ModelForm):
    class Meta:
        model = Wish

    def __init__(self, *args, **kwargs):
        super(WishForm, self).__init__(*args, **kwargs)
        self.fields['author'].required = True
        self.fields['event'].required = True
        self.fields['assigned_to'].required = True
        self.fields['wish_text'].required = True
