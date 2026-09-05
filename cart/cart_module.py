from django.shortcuts import get_object_or_404
from cart.models import Cart, CartItem, DiscountModel
from product.models import Product, Size, Color 
from django.utils import timezone


class CartManager:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.user = request.user if request.user.is_authenticated else None
        
        if self.user:
            self.cart, created = Cart.objects.get_or_create(user=self.user)
        else:
            self.cart = self._get_or_create_session_cart()

    def _get_or_create_session_cart(self):
        cart_id = self.session.get('cart_id')
        if cart_id:
            try:
                return Cart.objects.get(id=cart_id, user__isnull=True)
            except Cart.DoesNotExist:
                pass
        
        cart = Cart.objects.create(user=None)
        self.session['cart_id'] = cart.id
        return cart

    def add(self, product_id, size_id=None, color_id=None, quantity=1):
        product = get_object_or_404(Product, id=product_id)
        price = product.price  
        
        size = None
        color = None
    
        if size_id:
            size = get_object_or_404(Size, id=size_id)  
        if color_id:
            color = get_object_or_404(Color, id=color_id) 
        
        cart_item, created = CartItem.objects.get_or_create(
            cart=self.cart,
            product=product,
            size=size,
            color=color,
            defaults={'price': price, 'quantity': quantity}
        )
        
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        
        self.cart.updated_at = timezone.now()
        self.cart.save()
        return cart_item

    def remove(self, item_id):
        CartItem.objects.filter(id=item_id, cart=self.cart).delete()

    def update_quantity(self, item_id, quantity):
        cart_item = get_object_or_404(CartItem, id=item_id, cart=self.cart)
        if quantity <= 0:
            cart_item.delete()
        else:
            cart_item.quantity = quantity
            cart_item.save()

    def clear(self):
        self.cart.items.all().delete()
        self.cart.discount = None
        self.cart.save()

    def get_items(self):
        return self.cart.items.select_related('product').all()

    def get_total_price(self):
        return self.cart.get_total_price()

    def get_total_items(self):
        return self.cart.get_total_items()

    def get_cart_info(self):
        return {
            'items': self.get_items(),
            'total_price': self.cart.get_total_price(),
            'discount_amount': self.cart.get_discount_amount(),
            'final_price': self.cart.get_final_price(),
            'cart_id': self.cart.id
        }
        
    def apply_discount(self, discount_code):
        try:
            discount = DiscountModel.objects.get(name=discount_code, is_active=True)
            self.cart.discount = discount
            self.cart.save()
            
            discount.quantity -= 1
            discount.save()
            
            return True, f'Discount code "{discount_code}" applied successfully.'
        except DiscountModel.DoesNotExist:
            return False, f'Discount code "{discount_code}" is invalid or inactive.'

    def merge_carts(self):
        session_cart_id = self.session.get('cart_id')
        if session_cart_id and self.user:
            try:
                session_cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
                for item in session_cart.items.all():
                    cart_item, created = CartItem.objects.get_or_create(
                        cart=self.cart,
                        product=item.product,
                        size=item.size,
                        color=item.color,
                        defaults={
                            'price': item.price,
                            'quantity': item.quantity
                        }
                    )
                    if not created:
                        cart_item.quantity += item.quantity
                        cart_item.save()
                session_cart.delete()
                del self.session['cart_id']
            except Cart.DoesNotExist:
                pass