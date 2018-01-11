from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not Found.")
        except Product.MultipleObjectsReturned:
            instance = Product.objects.filter(slug=slug, active=True)
            return instance.first()
        except:
            raise Http404('hmm....')
        return instance


class ProductFeaturedListView(ListView):
    queryset = Product.objects.featured()
    template_name = 'products/list.html'


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.featured()
    template_name = 'products/featured-detail.html'


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/list.html', context)


def product_detail_view(request, pk=None):
    queryset = get_object_or_404(Product, pk=pk)
    context = {
        'object': queryset
    }
    return render(request, 'products/detail.html', context)
