from lib2to3.fixes.fix_input import context

from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'curso': 'Programação WEB com Django Framework ',
        'outro': 'Django é massa'
    }
    return render(request, 'index.html', context)

def contato(request):
    context = {
        '':''
    }
    return render(request, 'contato.html', context)

