"""
URL configuration for Estore project.

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
from shop import views 
from django.conf import settings
from django.conf.urls.static import static
from shop.controller import cart, wishlist, checkout

urlpatterns = [
    path('admin', admin.site.urls),
    path('',views.signup,name='signup'),
    path('login',views.login,name='login'),

    path('home',views.home,name='home'),
    path('hf',views.hf,name='hf'),
    path('logout',views.logout,name='logout'),

    path('Collections',views.Collections,name='Collections'),
    path('Collections/<str:slug>',views.Collectionsview,name='Collectionsview'),
    path('Collections/<str:cate_slug>',views.Collectionsview,name='Collectionsview'),
    path('Collections/<str:cate_slug>/<str:prod_slug>', views.productview, name='productview'),

    path('add-to-cart', cart.addtocart, name="addtocart"),
    path('Cart', cart.viewcart, name="cart"),
    path('update-cart', cart.updatecart, name='updatecart'),
    path('delete-cart-item', cart.deletecartitem, name='deletecartitem'),

    path('Wishlist', wishlist.index, name="wishlist"),
    path('add-to-wishlist', wishlist.addtowishlist, name="addtowishlist"),
    path('delete-wishlist-item', wishlist.deletewishlistitem, name="deletewishlistitem"),

    path('checkout', checkout.index, name="checkout"),
    path('place-order', checkout.placeorder, name="placeorder"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

