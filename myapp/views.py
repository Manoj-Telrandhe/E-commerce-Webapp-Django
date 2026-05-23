from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request,  'myapp/index.html', context)


def detail(request, slug):
    product = Product.objects.filter(slug=slug).first() 
    
    context = {
        'product' : product
    }
    
    return render(request, 'myapp/detail.html', context)

