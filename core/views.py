from django.shortcuts import render, redirect
from product.models import Product, Category
from django.db.models import Q
from django.contrib import messages



def home(request):
    context = {
        'products':Product.objects.all()[0:8] 
        }
    
    return render(request, 'core/frontpage.html', context)


def shop(request):

    products = Product.objects.all()
    categories = Category.objects.all()
    active_category = request.GET.get('category',)

    if active_category:
        products = products.filter(category__slug=active_category)


    query = request.GET.get('query', '')
            
    if query:
        products = products.filter(Q(name__icontains=query) | Q (description__icontains=query))



    context = {
            'categories':categories,
            'products':products,
            'active_category':active_category
    }
    return render(request, 'core/shop.html', context)


