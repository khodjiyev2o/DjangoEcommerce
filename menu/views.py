from django.shortcuts import render

from .forms import RegistrationForm,UserprofileForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
# Create your views here.

def menu(request):
    return render(request, 'menu.html')


def thelogin(request):
    return render(request, 'login.html')


def register(request):

    form = RegistrationForm()
    customer_form=UserprofileForm()
    if request.method == "POST":

        form = RegistrationForm(request.POST)
        customer_form=UserprofileForm(request.POST)

        if form.is_valid and customer_form.is_valid:
            user=form.save()

            customer=customer_form.save(commit=False)
            customer.customer=user

            customer.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(password=password, username=username)
            login(request,user)
            return HttpResponseRedirect('')

    return render(request, 'register.html',{"forms":form,"customer_form":customer_form})
