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
    
class CategoryDetailView(ListView):
    template_name = "product/category_detail.html"
    model = Product
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'])
    
class FilterProductsView(ListView):
    template_name = "product/category_detail.html"
    model = Product
    context_object_name = "products"

    def get_queryset(self):
        queryset = Product.objects.all()
        
        colors = self.request.GET.getlist('color')
        sizes = self.request.GET.getlist('size')
        if colors:
            queryset = queryset.filter(color__title__in=colors).distinct()
        if sizes:
            queryset = queryset.filter(size__title__in=sizes).distinct()
        return queryset