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

# detail page
class DetailsView(DetailView):
    template_name = "product/detail.html"
    model = Product
    slug_field = 'slug'
    slug_url_kwarg = 'slug'