from django.shortcuts import render
from django.http import JsonResponse 
from .cart import Cart
from myapp.models import Product
from django.shortcuts import get_object_or_404

# Create your views here.
def cart_add(request):
    cart = Cart(request)
    
    print("Add to cart button clicked in a backend")
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product_quantity = request.POST.get("product_quantity")
        print("Product added to the cart has an id:", product_id) 
        print("Product quantity:", product_quantity)
        
        # product = Product.objects.get(id=product_id)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, product_qty=product_quantity)
        cart_quantity = cart.__len__()
        
    return JsonResponse({'qty' : cart_quantity })


def cart_overview(request):
    cart = Cart(request)
    
    context = {
        'cart' : cart
    }
    return render(request, 'cart/cart-overview.html', context)


def cart_delete(request):
    cart = Cart(request)
    # if request.POST.get("action")=='post':
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        cart.delete(product_id=product_id)
        cart_quantity = cart.__len__()
        cart_total = cart.get_total_price()
        return JsonResponse({"qty":cart_quantity, "total":cart_total})