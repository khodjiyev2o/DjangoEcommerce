from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm, UserprofileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .models import Product,OrderItem
from django.views.generic.detail import DetailView

# Create your views here.


def layout(request):
    if request.user.is_authenticated:
        return render(request, 'layout.html')
    else:
        return redirect('login')


def checkout(request):
    if request.user.is_authenticated:
        return render(request, 'checkout.html')
    else:
        return redirect('login')


def cart(request):
    if request.user.is_authenticated:
        print(request.user.customer)
        orderitem = OrderItem.objects.all().filter(customer=request.user.customer)
        product = Product.objects.all()

        return render(request, 'cart.html',{'orderitem':orderitem,"product":product})
    else:
        return redirect('login')




def menu(request):
    if request.user.is_authenticated:
        product=Product.objects.all()
        return render(request, 'menu.html',{'products':product})
    else:
        return redirect('login')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'viewpage.html'
    context_object_name = "product"

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
