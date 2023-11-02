from django.shortcuts import render, redirect
from base.forms import ContatoForm

def home(request):
    return render(request, "index.html")

def contato(request):
    sucesso = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        sucesso = True
    contexto = {
        'sucesso': sucesso,
        'form': form,
    }
    
    return render(request, 'contato.html', contexto)

def admin_login(request):
    return redirect('/admin/login/')