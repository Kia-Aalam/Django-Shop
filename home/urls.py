from django.urls import path
#from . import views
from home.views import IndexView, ContactView, CheckoutView, CartView

urlpatterns = [
    path('', IndexView.as_view(), name='home'), 
    path('contact/', ContactView.as_view(), name='contact'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('cart/', CartView.as_view(), name='cart')
]