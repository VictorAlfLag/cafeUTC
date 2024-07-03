from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')

def evento(request):
    return render(request, 'evento.html')

def contacto(request):
    return render(request, 'contacto.html')
