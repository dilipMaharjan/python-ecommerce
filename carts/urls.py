from django.conf.urls import url

from .views import (
    cart_home,
    cat_update
)

urlpatterns = [
    url(r'^$', cart_home, name='home'),
    url(r'^update/$', cat_update, name='update'),
]
