from django.shortcuts import render, redirect

from carts.models import Cart
from products.models import Product


def cart_home(request):
    cart, new_session = Cart.objects.get_session_or_create(request)
    products = cart.products.all()
    total = 0
    for x in products:
        total += x.price
    cart.total = total
    cart.save()
    return render(request, 'carts/home.html', {})


def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show Message to User")
            return redirect('cart:home')
        cart, new_session = Cart.objects.get_session_or_create(request)
        if product_obj in cart.products.all():
            cart.products.remove(product_obj)
        else:
            cart.products.add(product_obj)
    # return redirect(product_obj.get_absolute_url())
    return redirect('cart:home')
