

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from shop import views

from shop.views import login_view , load_views_login, product_listing



urlpatterns = [
    path("admin/", admin.site.urls),
    path('', product_listing, name='shop'),
    path('handle-button/', views.handle_button, name='handle_button'),
    path('my-account/', views.my_account, name='my_account'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', load_views_login, name='login'),
    path('upload-file/', views.search_products_by_image, name='upload_file'),
    path('paginate-products/', views.paginate_products, name='paginate_products'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




