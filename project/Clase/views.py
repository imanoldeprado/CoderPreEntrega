from django.shortcuts import render, redirect

from . import models, forms

def home(request):
    query = models.Comision.objects.all()
    context = {"comisiones": query}
    return render(request, "Clase/index.html", context)

def clase_create(request):
    if request.method == "POST":
        form = forms.ClaseForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("clase:home")
    else: #request.method == "GET"
        form = forms.ClaseForm()
    return render(request, "clase/clase_create.html", context= {"form": form})
