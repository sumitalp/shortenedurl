from django import forms
from django.forms import ModelForm
from urlprocessing.models import ShortenedUrl


class ShortenedUrlForm(ModelForm):
    # The picklist showing allowable groups to which a new list can be added
    # determines which groups the user belongs to. This queries the form object
    # to derive that list.
    def __init__(self, *args, **kwargs):
        super(ShortenedUrlForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ShortenedUrl
        fields = ['original_url']