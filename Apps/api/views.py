from django.shortcuts import render

from django.http import JsonResponse
from . models import Product

def index(request):
    products={}
    products=Product.objects.all()
    products_list = list(products.values()) 
    return JsonResponse(products_list, safe=False)
