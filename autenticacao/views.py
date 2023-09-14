from django.http import HttpResponse
from django.shortcuts import render, redirect
from .utils import password_is_valid
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages, auth

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
            user = User.objects.create_user(username = usuario, password = senha, is_active = False, email=email)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuario cadastrado com Sucesso')
            return redirect('logar')
        except:
            messages.add_message(request, constants.ERROR, 'Erro! Senha inválida. Tente novamente')
            return redirect('cadastro')

def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('auth/')
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')

        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Usuario ou Senha Inválidos')
            return redirect('/auth/logar')
        else:
            auth.login(request, usuario)
            return render(request, 'home.html')
    
def homepage(request):
        return render(request, 'home.html')