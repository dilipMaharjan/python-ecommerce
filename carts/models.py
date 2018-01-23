from django.conf import settings
from django.db import models
from django.db.models.signals import m2m_changed, pre_save

from products.models import Product

User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):

    def get_session_or_create(self, request):
        cart_id = request.session.get('cart_id', None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_session = False
            cart = qs.first()
            if request.user.is_authenticated() and cart.user is None:
                cart.user = request.user
                cart.save()
        else:
            cart = Cart.objects.new_session(user=request.user)
            new_session = True
            request.session['cart_id'] = cart.id

        return cart, new_session

    def new_session(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated():
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    products = models.ManyToManyField(Product)
    total = models.DecimalField(default=0.0, max_digits=100, decimal_places=2)
    subtotal = models.DecimalField(default=0.0, max_digits=100, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = CartManager()

    def __str__(self):
        return str(self.id)


def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products = instance.products.all()
        total = 0
        for product in products:
            total += product.price
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()


m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)


def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    instance.total = instance.subtotal


pre_save.connect(pre_save_cart_receiver, sender=Cart)
