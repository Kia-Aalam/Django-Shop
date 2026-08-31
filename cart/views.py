from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.contrib import messages

from .cart_module import CartManager


class CartDetailView(View):
    def get(self, request):
        cart_manager = CartManager(request)
        cart_info = cart_manager.get_cart_info()
        
        context = {
            'items': cart_info['items'],
            'total_price': cart_info['total_price'],
            'total_items': cart_info['total_items'],
        }
        return render(request, 'cart/cart_detail.html', context)


class CartAddView(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        size_id = request.POST.get('size')
        color_id = request.POST.get('color') 
        quantity = int(request.POST.get('quantity', 1))
        
        if not all([product_id, size_id, color_id]):
            messages.error(request, 'Please fill in all the fields')
            return redirect(request.META.get('HTTP_REFERER', 'product_list'))
        
        cart_manager = CartManager(request)
        cart_manager.add(product_id, size_id, color_id, quantity)
        
        messages.success(request, 'Product added to shopping cart')
        
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'message': 'Product added'})
        return redirect('cart_detail')


class CartRemoveView(View):
    def post(self, request, item_id):
        cart_manager = CartManager(request)
        cart_manager.remove(item_id)
        messages.success(request, 'The product has been removed from the shopping cart')
        return redirect('cart_detail')


class CartUpdateView(View):
    def post(self, request, item_id):
        quantity = int(request.POST.get('quantity', 0))
        cart_manager = CartManager(request)
        cart_manager.update_quantity(item_id, quantity)
        
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            cart_info = cart_manager.get_cart_info()
            return JsonResponse({
                'success': True,
                'item_total': cart_manager.cart.items.get(id=item_id).get_total_price(),
                'total_price': cart_info['total_price'],
                'total_items': cart_info['total_items']
            })
        return redirect('cart_detail')


class CartClearView(LoginRequiredMixin, View):
    def post(self, request):
        cart_manager = CartManager(request)
        cart_manager.clear()
        messages.success(request, 'The shopping cart has been emptied')
        return redirect('cart_detail')