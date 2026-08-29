from django.urls import path
#from . import views
from home.views import IndexView, ContactView, CartView

urlpatterns = [
    path('', IndexView.as_view(), name='home'), 
    path('contact/', ContactView.as_view(), name='contact'),
    path('cart/', CartView.as_view(), name='cart')
]