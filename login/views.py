from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from login.forms import SigninForm, SignupForm, OtpForm, RegisterForm, CheckoutForm
from login.models import CheckoutModel, Otp
from login.utils import send_otp_email
# class base view
from django.views.generic.edit import FormView
from django.contrib.auth.views import LogoutView
from django.views import View

from random import randint
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator

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
        else:
            messages.error(self.request, "The Username or Password is incorrect!")
            return self.form_invalid(form)
    
# register page
class RegisterView(View):
    
    @method_decorator(ratelimit(key='post:email', rate='2/5m', block=True, method='POST'))
    @method_decorator(ratelimit(key='post:email', rate='1/10m', block=True, method='POST'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request):
        form = RegisterForm()
        return render(request, "login/register.html", {'form':form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            randcode = randint(1000, 9999)
            #send_otp_email(form.cleaned_data['email'], randcode)
            Otp.objects.create(email=form.cleaned_data['email'], code=randcode)
            print(randcode)
            return redirect(reverse('otp') + f'?email={form.cleaned_data['email']}')
            
        return render(request, "login/register.html", {'form':form})

# otp
class OtpView(View):
    def get(self, request):
        form = OtpForm()
        return render(request, "login/otp.html", {'form': form})
    
    def post(self, request):
        email = request.GET.get('email')
        form = OtpForm(request.POST)
        
        if form.is_valid():
            otp_record = Otp.objects.filter(email=email, code=form.cleaned_data['code']).first()
            
            if otp_record and not otp_record.is_expired():
                User = get_user_model()
                otp_record.delete()
                
                if User.objects.filter(email=email).exists():
                    user = User.objects.get(email=email)
                    login(request, user)
                    return redirect('home')
                else:
                    user = User.objects.create_user(email=email)
                    login(request, user)
                    return redirect('home')
            else:
                messages.error(request, "Invalid or expired OTP!")
                otp_record.delete()
                    
        return render(request, "login/otp.html", {'form': form})

def send_again_otp(request):
    email = request.GET.get('email')
    if email:
        messages.error(request, "The code has been send")
        randcode = randint(1000, 9999)
        #send_otp_email(email, randcode)
        Otp.objects.create(email=email, code=randcode)
        print(randcode)
        return redirect(reverse('otp') + f'?email={email}')
    else:
        return redirect('register')

# checkout page
class CheckoutView(View):
    def get(self, request):
        initial_data = {}
        if request.user.is_authenticated:
            last_checkout = CheckoutModel.objects.filter(user=request.user).first()
            if last_checkout:
                initial_data = {
                    'first_name': last_checkout.first_name,
                    'last_name': last_checkout.last_name,
                    'phone': last_checkout.phone,
                    'address': last_checkout.address,
                    'city': last_checkout.city,
                    'post_code': last_checkout.post_code,
                }
        
        form = CheckoutForm(initial=initial_data)
        return render(request, 'login/checkout.html', {'form': form})
    
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('signin')

        form = CheckoutForm(request.POST)
        if form.is_valid():
            checkout = form.save(commit=False)
            checkout.user = request.user 
            checkout.save()
            return redirect('home') 
        
        return render(request, 'login/checkout.html', {'form': form})
    
# signout
class SignoutView(LogoutView):
    next_page = "/"