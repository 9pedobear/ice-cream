from django.shortcuts import render

def index(request):
    return render(request, 'ice_cream/index.html')

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