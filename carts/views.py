from django.shortcuts import render

from carts.models import Cart


def cart_home(request):
    cart = Cart.objects.get_session_or_create(request)
    return render(request, 'carts/home.html', {})
