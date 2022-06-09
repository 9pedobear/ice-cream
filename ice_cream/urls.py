from django.urls import path
from .views import index, about, product, contact, service, gallery, create_product, login_user, register_user, logout_user

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('product/', product, name='product'),
    path('contact/', contact, name='contact'),
    path('service/', service, name='service'),
    path('gallery/', gallery, name='gallery'),
    path('create_product/', create_product, name='create_product'),
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
    path('logout/', logout_user, name='logout'),
]