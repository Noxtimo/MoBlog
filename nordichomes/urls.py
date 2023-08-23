"""
URL configuration for nordichomes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home, shop
from product.views import product
from cart.views import add_to_cart, cart, checkout, hx_menu_cart, update_cart
from users.views import register
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views
from users import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('admin/', admin.site.urls),
    path('', home, name='ecom-home',),
    path('cart/', cart, name='cart'),
    path('cart/checkout/', checkout, name='checkout'),
    path('shop/', shop, name='ecom-shop',),
    path('shop/<slug:slug>/', product, name='ecom-product',),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart',),
    path('hx_menu_cart/', hx_menu_cart, name='hx_menu_cart'),
    path('update_cart/<int:product_id>/<str:action>/', update_cart, name='update_cart'),
]

if settings.DEBUG:
    urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
