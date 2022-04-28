from django.forms import ModelForm
from .models import Tunning


class TunningForm(ModelForm):
    class Meta:
        model = Tunning
        fields = ['date', 'service']
