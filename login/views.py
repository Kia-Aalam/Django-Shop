from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.urls import reverse_lazy
from login.forms import SigninForm, SignupForm
from login.models import SignupModel
# class base view
from django.views.generic.edit import FormView
from django.contrib.auth.views import LogoutView

# signin page
class SigninView(FormView):
    template_name = "login/signin.html"
    form_class = SigninForm
    success_url = reverse_lazy("signin")

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
            return redirect('home')
        
        return super().form_valid(form)
    
# signup
class SignupView(FormView):
    template_name = "login/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("signup")
    
    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        User = get_user_model()
        user = User.objects.create_user(email=email, password=password)
        login(self.request, user)
        
        return redirect('home')
    
# signout
class SignoutView(LogoutView):
    next_page = "/"