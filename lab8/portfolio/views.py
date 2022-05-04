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
