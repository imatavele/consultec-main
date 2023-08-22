from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from accounts.forms import LoginForm


def loginUser(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("listProject")
            else:
                msg = 'Dados de acesso incorrectos'
        else:
            msg = 'Erro na validação do formulário'

    return render(request, "login.html", {"form": form, "msg": msg})
