from django.urls import path
from product.views import DetailsView, ShopView

urlpatterns = [
    path('shop/', ShopView.as_view(), name='shop'),
    path('detail/<slug:slug>', DetailsView.as_view(), name='detail'),
]