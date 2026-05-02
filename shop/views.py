from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):

    allprods = []
    chunk_size = 3

    # Get unique categories
    categories = Product.objects.values_list('category', flat=True).distinct()

    for category in categories:

        products = list(Product.objects.filter(category=category))

        # Create chunks for this category
        chunks = [products[i:i+chunk_size] for i in range(0, len(products), chunk_size)]

        # Store category name + its chunks
        allprods.append((category, chunks))

    return render(request, "shop/index.html", {
        "allprods": allprods
    })



def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def productview(request):
    return render(request,'shop/productview.html')

def checkout(request):
    return render(request,'shop/checkout.html')
