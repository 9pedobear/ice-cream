from django.shortcuts import render, redirect
from .models import Product, Employer
from .forms import ProductForm, UserLoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout



def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегались')
            return redirect('login')
        else:
            messages.error(request, 'Что-то пошло не так')
    else:
        form = UserCreationForm()
    return render(request, 'ice_cream/register.html', {'form': form})



def login_user(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Успех')
            return redirect('/')
        else:
            messages.error(request, 'Неудача')
    else:
        form = UserLoginForm()
    return render(request, 'ice_cream/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('/')




def index(request):
    products = Product.objects.all()[:4]
    employers = Employer.objects.all()[:4]
    context = {
        'products': products,
        'employers': employers
    }
    return render(request, 'ice_cream/index.html', context)

def about(request):
    return render(request, 'ice_cream/about.html')

def contact(request):
    return render(request, 'ice_cream/contact.html')

def gallery(request):
    return render(request, 'ice_cream/gallery.html')

def product(request):
    products = Product.objects.all()
    return render(request, 'ice_cream/product.html', {'products' : products})

def service(request):
    return render(request, 'ice_cream/service.html')


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'ice_cream/create_product.html', {'form': form})