from django.shortcuts import render, redirect
from django.views.generic import TemplateView
#from django.views.generic.edit import FormView

# signin page
class SigninView(TemplateView):
    template_name = "login/signin.html"