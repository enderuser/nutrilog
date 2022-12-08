from django.http import HttpResponse
from django.shortcuts import render, redirect
from .utils import password_is_valid
from django.contrib.auth.models import User

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('cadastro')
        
        try:
            user = User.objects.create_user(username = usuario, password = senha, is_active = False)
            user.save()
            return redirect('logar')
        except:
            return redirect('cadastro')

def logar(request):
    return HttpResponse('Vc está na pagina de login')