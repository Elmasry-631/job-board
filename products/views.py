from django.shortcuts import render
from .models import AddProduct
# Create your views here.
 

def products(request):
    products = AddProduct.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)

def product_detail(request, slug):
    product_detail = AddProduct.objects.get(slug=slug)
    context = {'product': product_detail}
    return render(request, 'product_detail.html', context)



