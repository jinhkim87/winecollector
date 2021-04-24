from django.forms import ModelForm
from .models import Year

class YearForm(ModelForm):
    class Meta:
        model = Year
        fields = ['year']