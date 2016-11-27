from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def asnef(request):
    return render(request, 'asnef.html')

def coche(request):
    return render(request, 'coche.html')

def hipotecario(request):
    return render(request, 'hipotecario.html')

def microcredito(request):
    return render(request, 'microcredito.html')

def personal(request):
    return render(request, 'personal.html')

