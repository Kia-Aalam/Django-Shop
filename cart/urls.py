from django.urls import path
from cart.views import CartDetailView, CartAddView, CartRemoveView,  CartUpdateView, CartClearView

urlpatterns = [
    path('', CartDetailView.as_view(), name='cart_detail'),
    path('add/', CartAddView.as_view(), name='cart_add'),
    path('remove/<int:item_id>/', CartRemoveView.as_view(), name='cart_remove'),
    path('update/<int:item_id>/', CartUpdateView.as_view(), name='cart_update'),
    path('clear/', CartClearView.as_view(), name='cart_clear'),
]