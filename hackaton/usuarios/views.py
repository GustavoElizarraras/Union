from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView

#Models
from django.contrib.auth.models import User

#Forms
from usuarios.forms import SignupForm

def login_view(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'usuarios/login.html', {'error' : 'Usuario o contraseña invalidos'})
    return render(request, 'usuarios/login.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()

    return render(
        request=request,
        template_name='usuarios/signup.html',
        context={'form': form}
    )


@login_required
def logout_view(request):

    logout(request)
    return redirect('login')