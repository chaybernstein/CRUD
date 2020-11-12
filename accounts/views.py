from django.shortcuts import render

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

def cadastro(request):
    return render(request, 'accounts/cadastro.html')

def alterar(request):
    return render(request, 'accounts/alterar.html')

def deletar(request):
    return render(request, 'accounts/deletar.html')