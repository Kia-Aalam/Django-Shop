from django.urls import path
#from . import views
'''from django.conf import settings
from django.conf.urls.static import static'''
from home.views import IndexView, ContactView, CheckoutView, CartView

urlpatterns = [
    path('', IndexView.as_view(), name='home'), 
    path('contact/', ContactView.as_view(), name='contact'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('cart/', CartView.as_view(), name='cart')
]
'''if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)'''