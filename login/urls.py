from django.urls import path
from login.views import SigninView

urlpatterns = [
    path('', SigninView.as_view(), name='signin'), 
]