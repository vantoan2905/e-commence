from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from shop.models import Product

import random
import json

def product_listing(request):
    products = Product.objects.order_by('?')[:32]
    return render(request, 'shop/shop_view.html', {'products': products})

def report_search(search_value):
    # Placeholder for logging or analytics functionality
    pass

@csrf_exempt
def handle_button(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            search_value = data.get('search', '').strip()
            report_search(search_value)
            products = Product.objects.filter(productDisplayName__icontains=search_value)
            product_list = [
                {'name': product.productDisplayName, 'price': product.price, 'image': product.image.url}
                for product in products[:32]
            ]
            return JsonResponse({'products': product_list})
        except (ValueError, KeyError):
            return JsonResponse({'error': 'Invalid data'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def my_account(request):
    if request.user.is_authenticated:
        return render(request, 'shop/my_account.html', {'user': request.user})
    return redirect('login_view')

def logout_view(request):
    logout(request)
    return redirect('login_view')
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            products = Product.objects.order_by('?')[:32]
            print ("Login successful for user:", user.username)
            return render(request, 'shop/shop_view.html', {'products': products})
        messages.error(request, "Invalid username or password.")
    return render(request, 'shop/login.html')
