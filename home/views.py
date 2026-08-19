from django.shortcuts import render, redirect
from home.forms import ContactForm
from home.models import ContactModel
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

# index page
class index(TemplateView):
    template_name = "index.html"

# contact page
class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        ContactModel.objects.create(
            email=form.cleaned_data['email'],
            subject=form.cleaned_data['subject'],
            message=form.cleaned_data['message']
        )   
        return super().form_valid(form)