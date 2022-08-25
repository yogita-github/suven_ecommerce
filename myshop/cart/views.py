from django.shortcuts import render
from cart.cart import Cart
from cart.forms import CartAddProductForm



def cart_detail(request):
    cart=Cart(request)
    for item in cart:
        item['update_quantity_form']=CartAddProductForm(
            initial={'quantity':item['quantity'],
            'update':True})
    return render(request, 'cart/detail.html',{'cart':cart})

def cart_add(request):
    cart=Cart(request)
    return render(request,'cart/add.html',{'cart':cart})

def cart_remove(request):
    cart=Cart(request)
    return render(request,'cart/remove.html',{'cart':cart})

