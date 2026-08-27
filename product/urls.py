from django.urls import path
from product.views import DetailView, ShopView

urlpatterns = [
    path('shop/', ShopView.as_view(), name='shop'),
    path('detail/', DetailView.as_view(), name='detail'),
]