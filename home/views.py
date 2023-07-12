from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, "home/index.html")

def sobre(request):
    return render(request, "home/sobre.html")

def galeria(request):
    return render(request, "home/galeria.html")

def marcas(request):
    return render(request, "home/marcas.html")

def artes(request):
    return render(request, "home/artes.html")

def monstros(request):
    return render(request, "home/monstros.html")

def contato(request):
    if str(request.method) == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            messages.success(request, "E-mail enviado com sucesso.")
            form = ContactForm()
        else:
            messages.error(request, "Não foi possível enviar o e-mail.")
    else:
        form = ContactForm()
    context = {
        "form":form
    }
    return render(request, "home/contato.html", context)