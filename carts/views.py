from django.shortcuts import render

from carts.models import Cart


def create_cart():
    return Cart.objects.create(user=None)


def cart_home(request):
    cart_id = request.session.get('cart_id', None)
    if cart_id is None:
        cart = create_cart()
        request.session['cart_id'] = cart.id
        print("New Cart created")
    else:
        qs = Cart.objects.filter(id=cart_id)
        if qs.count() == 1:
            cart = qs.first()
        else:
            cart = create_cart()
            request.session['cart_id'] = cart.id
    return render(request, 'carts/home.html', {})
