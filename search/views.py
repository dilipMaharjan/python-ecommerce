from django.views.generic import ListView

from products.models import Product


class SearchProductView(ListView):
    template_name = 'search/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        if q is not None:
            return Product.objects.search(q)
        return Product.objects.featured()
