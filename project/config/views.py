from django.http import HttpResponse
from django.template import Context, Template

def saludo(request):
    return HttpResponse("Esta es mi primer View")

def segunda_vista(request):
    return HttpResponse("<h1> Segunda Vista </h1>")

def persona(request, nombre, apellido):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"{apellido}, {nombre}")

def probando_template(request):
    mi_html = open("./templates/template1.html", encoding="utf-8")
    mi_template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context({"saludo": "¡Bienvenido!", "autor": "Coderhouseeee"})
    mi_documento = mi_template.render(mi_contexto)
    return HttpResponse(mi_documento)