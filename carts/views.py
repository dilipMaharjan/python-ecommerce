from django.shortcuts import render

from carts.models import Cart


def cart_home(request):
    cart_id = request.session.get('cart_id', None)
    if cart_id is None:
        cart = Cart.objects.new_session(user=request.user)
        request.session['cart_id'] = cart.id
        print("New Cart created")
    else:
        qs = Cart.objects.filter(id=cart_id)
        if qs.count() == 1:
            cart = qs.first()
            if request.user.is_authenticated() and cart.user is None:
                cart.user = request.user
                cart.save()
        else:
            cart = Cart.objects.new_session(user=request.user)
            request.session['cart_id'] = cart.id
    return render(request, 'carts/home.html', {})
