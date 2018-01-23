from django.shortcuts import render, redirect

from carts.models import Cart
from products.models import Product


def cart_home(request):
    cart = Cart.objects.get_session_or_create(request)
    return render(request, 'carts/home.html', {})


def cat_update(request):
    product_id = 1
    product_obj = Product.objects.get(id=product_id)
    cart, new_obj = Cart.objects.get_session_or_create(request)
    cart.products.add(new_obj)
    # return redirect(product_obj.get_absolute_url())
    return redirect('cart:home')
