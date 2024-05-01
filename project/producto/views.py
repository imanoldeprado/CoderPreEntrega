from django.shortcuts import render, redirect

# Create your views here.
from . import models, forms

def home(request):
    consulta_productos = models.ProductoCategoria.objects.all
    context = {"productos": consulta_productos}
    return render(request, "producto/index.html", context)

def productocategoria_create(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("producto:home")
    else: #request.method == "GET"
        form = forms.ProductoCategoriaForm()
    return render(request, "producto/productocategoria_create.html", context= {"form": form})