from django.shortcuts import render, redirect

from carts.models import Cart
from orders.models import Order
from products.models import Product


def cart_home(request):
    cart, new_session = Cart.objects.get_session_or_create(request)
    return render(request, 'carts/home.html', {'cart': cart})


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

        request.session['cart_items'] = cart.products.count()
    # return redirect(product_obj.get_absolute_url())
    return redirect('cart:home')


def cart_checkout(request):
    cart_obj, cart_created = Cart.objects.get_session_or_create(request)
    if cart_created or cart_obj.products.count() == 0:
        return redirect('cart:home')
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    return render(request, 'carts/checkout.html', {"object": order_obj})
