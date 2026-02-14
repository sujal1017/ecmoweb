from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):

    products = list(Product.objects.all())

    chunk_size = 3

    # Create chunks
    chunks1 = [products[i:i+chunk_size] for i in range(0, len(products), chunk_size)]
    chunks2 = [products[i:i+chunk_size] for i in range(0, len(products), chunk_size)]

    # Store both inside one list
    allprods = [chunks1, chunks2]

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
