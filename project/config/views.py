from django.http import HttpResponse
#from django.template import Context, Template
from django.shortcuts import render

def saludo(request):
    return HttpResponse("Esta es mi primer View")

def segunda_vista(request):
    return HttpResponse("<h1> Segunda Vista </h1>")

def persona(request, nombre, apellido):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"{apellido}, {nombre}")

#def probando_template(request):
    mi_html = open("./templates/template1.html", encoding="utf-8")
    mi_template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context({"saludo": "¡Bienvenido!", "autor": "Coderhouseeee"})
    mi_documento = mi_template.render(mi_contexto)
    return HttpResponse(mi_documento)

def probando_template(request):
    mi_contexto = {"saludo": "¡Bienvenido!", "autor": "Probando 1 2 3"}
    return render(request, "template1.html", mi_contexto)

def template_notas(request):
    lista_de_notas = [9,7,4,5,6,8,3,7,2]
    contexto = {"notas": lista_de_notas}
    return render(request, "template_de_notas.html", contexto)

def persona_edad(request):
    formulario = {
        "persona":{
            "nombre": "Imanol",
            "edad": 29
        },    
    }
    return render(request, "template_censo.html", context = formulario)