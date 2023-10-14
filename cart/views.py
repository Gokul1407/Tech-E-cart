from django.shortcuts import get_object_or_404, redirect, render
from store.models import Product
from cart.models import Cart, CartItem
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from decimal import Decimal

# Create your views here.
@login_required
def view_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.cartitem_set.all()

        # Calculate total price
        total_price = sum(item.sub_total() for item in cart_items)

        # Calculate tax (assuming 2% tax)
        tax = Decimal('0.02') * total_price

        # Calculate the overall total (total price + tax)
        overall_total = total_price + tax

    except Cart.DoesNotExist:
        cart = None
        cart_items = []
        total_price = Decimal(0)
        tax = Decimal(0)
        overall_total = Decimal(0)

    return render(request, 'cart.html', {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': total_price,
        'tax': tax,
        'overall_total': overall_total,
    })

@login_required
def add_to_cart(request,product_id):
    
    products=Product.objects.get(id=product_id)
    cart , created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=products)
    if not item_created:
        cart_item.quantity += 1
        
        cart_item.save()

    return redirect('view_cart')

def decrease_quantity(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created and cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()

    return redirect('view_cart')


def remove_item(request, product_id):
    products=Product.objects.get(id=product_id)
    cart , created = Cart.objects.get_or_create(user=request.user)
    try:
        cart_item = CartItem.objects.get(cart=cart, product=products)
        cart_item.delete()  # Delete the cart item
    except CartItem.DoesNotExist:
        pass

    return redirect('view_cart')
    