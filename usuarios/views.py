from django.shortcuts import redirect, render

from usuarios.forms import LoginForms, CadastroForms

def login(request):
    form = LoginForms()
    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()
    
    if request.method == 'post':
        form = CadastroForms(request.POST)
        
        if form["senha_1"].value() != form["senha_2"].value():
            return redirect('cadastro')
    
    return render(request, "usuarios/cadastro.html", {"form": form})