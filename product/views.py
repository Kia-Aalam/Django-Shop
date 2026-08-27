from django.shortcuts import render
from django.urls import reverse_lazy

from product.models import Product

# class base view
from django.views.generic import ListView, DetailView

# shop page
class ShopView(ListView):
    template_name = "product/shop.html"
    model = Product
    context_object_name = 'products'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        
        if q:
            queryset = queryset.filter(title__icontains=q)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q')
        return context

# detail page
class DetailsView(DetailView):
    template_name = "product/detail.html"
    model = Product
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
# search result page
class SearchResultView(ListView):
    template_name = "product/search_result.html"
    model = Product
    context_object_name = 'products'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        
        if q:
            queryset = queryset.filter(title__icontains=q)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q')
        return context