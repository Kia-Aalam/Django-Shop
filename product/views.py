from django.shortcuts import render
from django.urls import reverse_lazy
# class base view
from django.views.generic import TemplateView

# shop page
class ShopView(TemplateView):
    template_name = "product/shop.html"
    
# detail page
class DetailView(TemplateView):
    template_name = "product/detail.html"
    