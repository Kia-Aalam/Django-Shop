from django.urls import path
from product.views import DetailsView, ShopView, SearchResultView, CategoryDetailView, FilterProductsView

urlpatterns = [
    path('shop/', ShopView.as_view(), name='shop'),
    path('detail/<slug:slug>', DetailsView.as_view(), name='detail'),
    path('search/', SearchResultView.as_view(), name='search'),
    path('category/<slug:category_slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('filter/', FilterProductsView.as_view(), name='filter_products')
]