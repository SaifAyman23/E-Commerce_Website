from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Cart,Cart_item,Coupon,Variation
from store.models import Product
# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
   
def add_item(request,item_id):
    print("ADDING THE ITEM")
    user = request.user
    print(item_id)   
    cart_item = Cart_item.objects.get(id=item_id,user=user)
    print('================')
    print(cart_item)
    print('================')
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:cart') 

def remove_cart_item(request,item_id,):
    print("DELETING ITEM")
    cart_item = Cart_item.objects.get(id=item_id,user=request.user)
    variation=Variation.objects.get(id=str(cart_item.variations))
    if cart_item.quantity >1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
        variation.delete()
    return redirect('cart:cart')

def remove_cart(request,item_id):
    print("REMOVEEEE")
    cart_item = Cart_item.objects.get(id=item_id,user=request.user)
    variation=Variation.objects.get(id=str(cart_item.variations))
    cart_item.delete()
    variation.delete()
    return redirect('cart:cart')

@login_required(login_url='accounts:login')
def cart(request,total=0,quantity=0,grand_total=0,coupon=None,discount=0):
    print("IN THE CART!!!!!!")
    try:
        cart_items = Cart_item.objects.all().filter(user=request.user,is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price)*cart_item.quantity
            quantity += cart_item.quantity
        if request.method == "POST":
            discount = request.POST['coupon']
            if discount:
                try:
                    coupon = Coupon.objects.get(value=discount)
                    shipping = 20   
                    grand_total = shipping+total 
                    discount = (grand_total*coupon.ratio)/100
                    grand_total = grand_total-discount
                except:
                    pass 
        else:            
            shipping = 20   
            grand_total = shipping+total 
        
    except Cart_item.DoesNotExist:
        pass
    print(total)
    context = {
        'cart_items':cart_items,
        'total':total,
        'quantity':quantity,
        'grand_total':grand_total,
        'shipping': shipping,
        'discount':discount,
    }
    return render(request,'cart/cart.html',context)




