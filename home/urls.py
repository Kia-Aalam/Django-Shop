from django.urls import path
#from . import views
from home.views import IndexView, ContactView

urlpatterns = [
    path('', IndexView.as_view(), name='home'), 
    path('contact/', ContactView.as_view(), name='contact'),
]