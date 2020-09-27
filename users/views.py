from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import NewUserRegisterForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = NewUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт успешно создан для {username}')
            return redirect('login')
    else:
        form = NewUserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def success_registration(request):
    return render(request, 'users/success_registration.html')


def success_login(request):
    return render(request, 'users/success_login.html')
