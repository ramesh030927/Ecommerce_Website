from django.shortcuts import render
from .models import Product, ContactInfo

def index(request):
    products = Product.objects.filter(in_stock=True).order_by('-created_at')
    contact = ContactInfo.objects.last()
    return render(request, 'index.html', {'products': products, 'contact': contact})
