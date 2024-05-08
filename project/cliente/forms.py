from django import forms
from . import models

#class ProductoCategoriaForm(forms.Form):
    #Especificar los campos
    #nombre = forms.CharField()
    #descripcion = forms.CharField()
    
class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }