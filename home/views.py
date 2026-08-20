from django.shortcuts import render, redirect
from home.forms import ContactForm
from home.models import ContactModel
from django.urls import reverse_lazy
# class base view
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

# index page
class IndexView(TemplateView):
    template_name = "index.html"

# contact page
class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        ContactModel.objects.create(
            email=form.cleaned_data['email'],
            subject=form.cleaned_data['subject'],
            message=form.cleaned_data['message']
        )   
        return super().form_valid(form)
    
# detail page
class DetailView(TemplateView):
    template_name = "detail.html"
    
# shop page
class ShopView(TemplateView):
    template_name = "shop.html"
    
# checkout page
class CheckoutView(TemplateView):
    template_name = "checkout.html"
    
# cart page
class CartView(TemplateView):
    template_name = "cart.html"