"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from .views import home, hello_world, about, contact, login_page, register_page
from products.views import (
    product_list_view,
    product_detail_view,
    ProductListView,
    ProductDetailView,
    ProductFeaturedListView,
    ProductFeaturedDetailView,
    ProductDetailSlugView
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello_world),
    url(r'^$', home),
    url(r'^about/$', about),
    url(r'^contact/$', contact),
    url(r'^login/$', login_page),
    url(r'^register/$', register_page),
    url(r'^products/$', ProductListView.as_view()),
    # url(r'^products/(?P<pk>\d+)/$', ProductDetailSlugView.as_view()),
    url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    url(r'^featured/$', ProductFeaturedListView.as_view()),
    url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
    url(r'^products-fbv/$', product_list_view),
    url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
