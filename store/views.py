from django.shortcuts import render
from store.models import Product
from home.models import Category

# Create your views here.
def store(request):
    products=Product.objects.all()
    return render(request,'store.html',{'products':products})

def category_sort(request,category_slug):
    category = Category.objects.get(category_slug=category_slug)
    sorted_products = Product.objects.filter(category=category)
    return render(request,'store.html',{'products':sorted_products})

def product_details(request,product_slug):
    products=Product.objects.get(product_slug=product_slug)
    return render(request,'product_details.html',{'products':products})

