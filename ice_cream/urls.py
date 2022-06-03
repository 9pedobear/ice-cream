from django.urls import path
from .views import index, about, product, contact, service, gallery

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('product/', product, name='product'),
    path('contact/', contact, name='contact'),
    path('service/', service, name='service'),
    path('gallery/', gallery, name='gallery'),
]