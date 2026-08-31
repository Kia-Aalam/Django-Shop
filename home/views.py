from django.shortcuts import render, redirect
from home.forms import ContactForm
from home.models import ContactModel
from product.models import Product
from django.urls import reverse_lazy
# class base view
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView

# index page
class IndexView(ListView):
    template_name = "index.html"
    model = Product
    context_object_name = "products"

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