from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    # grab all products and store them in a variable names 'products
    products = Product.objects.all()
    # use render to tell django to request the index.html template. Use products variable to display products
    return render(request, 'index.html', {'products': products})


def new_products(request):
    return HttpResponse('These are new products')

