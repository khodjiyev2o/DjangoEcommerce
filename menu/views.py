from django.shortcuts import render


# Create your views here.

def menu(request):
    return render(request, 'menu.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
