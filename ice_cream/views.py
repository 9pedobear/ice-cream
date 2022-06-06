from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse

def index(request):
    products = Product.objects.all()
    return render(request, 'ice_cream/index.html', {'products':products})

def about(request):
    return render(request, 'ice_cream/about.html')

def contact(request):
    return render(request, 'ice_cream/contact.html')

def gallery(request):
    return render(request, 'ice_cream/gallery.html')

def product(request):
    return render(request, 'ice_cream/product.html')

def service(request):
    return render(request, 'ice_cream/service.html')

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            ice_cream = form.save()
            return redirect(ice_cream)
    else:
        form = ProductForm()
    return render(request, 'ice_cream/create_product.html', {'prod':form})