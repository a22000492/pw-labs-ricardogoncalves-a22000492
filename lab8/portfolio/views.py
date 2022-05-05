from datetime import datetime

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home_page_view(request):
    agora = datetime.datetime.now()
    context = {
        'data': agora.date,
    }

    return render(request, 'portfolio/home.html', context)

def apresentacao(request):
    return render(request, 'portfolio/apresentacao.html')

def competencias(request):
    return render(request, 'portfolio/competencias.html')

def formacao(request):
    return render(request, 'portfolio/formacao.html')

def projetos(request):
    return render(request, 'portfolio/projetos.html')
