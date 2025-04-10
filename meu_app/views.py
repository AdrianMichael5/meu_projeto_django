from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def pagina_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(request, username=username, password=senha)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'usuarios/login.html', {'erro': 'Credenciais inválidas'})
    return render(request, 'usuarios/login.html')

def pagina_cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'usuarios/cadastro.html', {'erro': 'Usuário já existe'})

        User.objects.create_user(username=username, email=email, password=senha)

        user = authenticate(request, username=username, password=senha)
        if user:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'usuarios/cadastro.html')


def dashboard(request):
    return render(request, 'usuarios/dashboard.html')

def sair(request):
    logout(request)
    return redirect('login')