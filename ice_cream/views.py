from django.shortcuts import render, redirect
from .models import Product, Employer
from .forms import ProductForm
from django.http import HttpResponse

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