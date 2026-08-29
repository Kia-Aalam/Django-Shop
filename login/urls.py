from django.urls import path
from login.views import SigninView, SignoutView, SignupView, OtpView, RegisterView, send_again_otp, CheckoutView

urlpatterns = [
    path('signin/', SigninView.as_view(), name='signin'), 
    path('signout/', SignoutView.as_view(), name='signout'), 
    path('signup/', SignupView.as_view(), name='signup'),
    path('register/', RegisterView.as_view(), name='register'),
    path('otp/', OtpView.as_view(), name='otp'),
    path('send-again-otp/', send_again_otp, name='send_again_otp'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]