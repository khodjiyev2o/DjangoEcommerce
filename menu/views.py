from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm, UserprofileForm, UserUpdateForm, UpdationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .models import Product, OrderItem, Order, Customer
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .filters import ProductFilter
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import View


from django.shortcuts import get_object_or_404

# Create your views here.


@login_required(login_url='login')
def layout(request):
    order, created = Order.objects.get_or_create(customer=request.user.customer)
    return render(request, 'layout.html',{'order':order})


@login_required(login_url='login')
def checkout(request):
    order = Order.objects.get(customer=request.user.id)
    orderitem = OrderItem.objects.filter(order=order)
    return render(request, 'checkout.html', {'order': order, 'orderitem': orderitem})


@login_required(login_url='login')
def cart(request):
    order, created = Order.objects.get_or_create(customer=request.user.customer)

    # orderitem=OrderItem.objects.filter(order=order)
    orderitem = order.orderitem_set.all()
    return render(request, 'cart.html', {'orderitem': orderitem, 'order': order})


@login_required(login_url='login')
def menu(request):
    order, created = Order.objects.get_or_create(customer=request.user.customer)
    product = Product.objects.all()
    myFilter = ProductFilter(request.GET, queryset=product)
    product = myFilter.qs

    return render(request, 'menu.html', {'products': product,'order':order, 'myFilter': myFilter})


class ProductDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Product
    template_name = 'viewpage.html'
    context_object_name = "product"


@unauthenticated_user
def thelogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            messages.success(request, ('There was an error!'))
            return redirect('login')
    else:
        return render(request, 'login.html')


@unauthenticated_user
def register(request):
    form = RegistrationForm()
    customer_form = UserprofileForm()
    if request.method == "POST":

        form = RegistrationForm(request.POST)
        customer_form = UserprofileForm(request.POST)

        if form.is_valid and customer_form.is_valid:
            user = form.save()

            customer = customer_form.save(commit=False)
            customer.customer = user

            customer.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(password=password, username=username)
            login(request, user)
            return HttpResponseRedirect('/')

    return render(request, 'register.html', {"forms": form, "customer_forms": customer_form})


def logout_user(request):
    logout(request)
    messages.warning(request, 'You have been logged out!')
    return redirect('login')


@login_required(login_url='login')
def profileupdate(request, pk):
    if request.method == "POST":

        userform = UserUpdateForm(request.POST, instance=request.user)
        customer_form = UpdationForm(request.POST, request.FILES, instance=request.user.customer)

        if userform.is_valid and customer_form.is_valid:
            user = userform.save()

            customer = customer_form.save(commit=False)
            customer.customer = user

            customer.save()

            return HttpResponseRedirect('/')
    else:
        userform = UserUpdateForm(instance=request.user)
        customer_form = UpdationForm(instance=request.user.customer)
    return render(request, 'profile.html', {"forms": userform, "customer_forms": customer_form})


class SuperUserCheck(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser


class AuthorCreateView(SuperUserCheck, CreateView):
    model = Product
    fields = '__all__'
    template_name = 'admin.html'
    success_url = '/'


class AuthorUpdateView(SuperUserCheck, UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'admin.html'
    success_url = '/'


class AuthorDeleteView(SuperUserCheck, DeleteView):
    model = Product
    template_name = 'delete.html'
    success_url = '/'
    fields = '__all__'


class CustomerView(SuperUserCheck, ListView):
    model = Customer
    template_name = 'customers.html'
    context_object_name = "customers"
    success_url = '/'
    queryset = Customer.objects.exclude(customer=1)



