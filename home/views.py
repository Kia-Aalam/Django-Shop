from django.shortcuts import render, redirect
from home.forms import ContactForm
from home.models import ContactModel
from product.models import Product, Type
from django.urls import reverse_lazy
# class base view
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView

# index page
class IndexView(ListView):
    template_name = "index.html"
    model = Product
    context_object_name = "products"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["types"] = Type.objects.all()
        return context

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