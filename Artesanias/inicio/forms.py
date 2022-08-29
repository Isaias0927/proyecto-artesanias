from django import forms
from .models import OpinionArtesania


class OpinionForm(forms.ModelForm):
    class Meta:
        model = OpinionArtesania
        fields = ('artesania', 'opinion')

class Arte(forms.ModelForm):
    class Meta:
        model = OpinionArtesania
        fields = ['artesania', 'opinion']