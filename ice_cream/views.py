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
    return render(request, 'ice_cream/product.html')

def service(request):
    return render(request, 'ice_cream/service.html')


def handle_uploaded_file(f):
    with open('media/images/'+f, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def create_product(request):
    context = {}
    if request.POST:
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.POST["image"])
            return redirect('/')
    else:
        form = ProductForm()
    context['prod'] = form
    return render(request, "ice_cream/create_product.html", context)