from django.shortcuts import render
from .models import Petshop
from .forms import ReservaForm

def reserva(request):
    sucesso = False
    form = ReservaForm(request.POST or None)
    if form.is_valid():
        form.save()
        sucesso = True
    
    contexto = {
        'form': form,
        'sucesso': sucesso,
    }

    return render(request, 'reserva.html', contexto)
