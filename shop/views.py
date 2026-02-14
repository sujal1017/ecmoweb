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
    return HttpResponse("We are at Contact")

def tracker(request):
    return HttpResponse("We are at Tracker")

def search(request):
    return HttpResponse("We are at Search")

def productview(request):
    return HttpResponse("We are at ProductView")

def checkout(request):
    return HttpResponse("We are at CheckOut")
