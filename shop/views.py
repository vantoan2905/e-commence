from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from shop.models import Product
import json
import base64
import os
from django.conf import settings
from shop.image_classifier import ImageClassifier

def product_listing(request):
    """
    Render the shop view page with a random selection of 32 products.
    """
    products = Product.objects.order_by('?')[:32]
    return render(request, 'shop/shop_view.html', {'products': products})

def report_search(search_value):
    # Placeholder for logging or analytics functionality
    pass

@csrf_exempt
def handle_button(request):
    """
    Handle button click for searching products by name.
    """
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

def load_views_login(request):
    return render(request, 'shop/login_view.html')

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            products = Product.objects.order_by('?')[:32]
            print("Login successful for user:", user.username)
            return render(request, 'shop/shop_view.html', {'products': products})
        messages.error(request, "Invalid username or password.")
    return render(request, 'shop/login_view.html')

def search_products_by_image(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            file_data = data.get('fileData')
            file_name = data.get('fileName', 'uploaded_file.jpg')

            if not file_data or ',' not in file_data:
                return JsonResponse({'status': 'error', 'message': 'No valid file provided.'})

            file_content = base64.b64decode(file_data.split(',')[1])
            upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
            os.makedirs(upload_dir, exist_ok=True)
            file_path = os.path.join(upload_dir, file_name)

            with open(file_path, 'wb') as f:
                f.write(file_content)

            model_path = os.path.join(settings.BASE_DIR, 'static/models/articleType_final.keras')
            label_mapping_path = os.path.join(settings.BASE_DIR, 'static/models/articleType.csv')


            result = ImageClassifier.image_classifier(file_path=file_path,
                                                      model=model_path,
                                                      label_mapping=label_mapping_path)

            if not result:
                return JsonResponse({'status': 'error', 'message': 'Failed to classify image.'})

            products = Product.objects.filter(productDisplayName__icontains=result)
            product_list = [
                {'name': product.productDisplayName, 'price': product.price, 'image': product.image.url}
                for product in products[:32]
            ]
            os.remove(file_path)
            return JsonResponse({'products': product_list})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Unexpected error: {str(e)}'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method. Use POST.'})

def paginate_products(request):
    return JsonResponse({'status': 'success', 'message': 'Pagination is working!'})
