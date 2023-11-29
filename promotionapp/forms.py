from django import forms
from promotionapp.models import Services

class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields =['name','cost','description']