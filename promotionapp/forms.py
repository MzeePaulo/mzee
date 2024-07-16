from django import forms
from promotionapp.models import Services,DesignModel

class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields =['name','cost','description']


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = DesignModel
        fields = ['image', 'title', 'price']