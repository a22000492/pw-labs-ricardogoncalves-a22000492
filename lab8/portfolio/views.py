from datetime import datetime

# Create your views here.
from django.shortcuts import render

def home_page_view(request):
    agora = datetime.now()
    context = {
        'data': agora.date,
    }

    return render(request, 'portfolio/home.html', context)

def apresentacao_page_view(request):
    return render(request, 'portfolio/apresentacao.html')

def competencias_page_view(request):
    return render(request, 'portfolio/competencias.html')

def formacao_page_view(request):
    return render(request, 'portfolio/formacao.html')

def projetos_page_view(request):
    return render(request, 'portfolio/projetos.html')

def licenciatura_page_view(request):
    return render(request, 'portfolio/licenciatura.html')
