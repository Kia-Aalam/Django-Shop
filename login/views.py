from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from login.forms import SigninForm


class SigninView(FormView):
    template_name = "login/signin.html"
    form_class = SigninForm
    success_url = "/signin/" #check this

    '''def form_valid(self, form):
        ContactModel.objects.create(
            email=form.cleaned_data['email'],
            subject=form.cleaned_data['subject'],
            message=form.cleaned_data['message']
        )   
        return super().form_valid(form)'''