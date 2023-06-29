from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Cart, CartItem
from django.views.generic import DetailView

def landing_page(request):
    return render(request, 'shop/landing-page.html')

def menu_page(request):
    product = Product.objects.first()
    return render(request, 'shop/menu-page.html', {'product': product})

def proteins_page(request):
    category = Category.objects.get(name='ProteinPowder')
    products = category.product_set.all()
    context = {'products': products}

    return render(request, 'shop/proteins-page.html', context)

def equipment_page(request):
    category = Category.objects.get(name='GymEquipment')
    products = category.product_set.all()
    context = {'products': products}

    return render(request, 'shop/proteins-page.html', context)

def suplements(request):
    category = Category.objects.get(name='Supplement')
    products = category.product_set.all()
    context = {'products': products}

    return render(request, 'shop/proteins-page.html', context)

def workout_plans(request):
    category = Category.objects.get(name='WorkoutPlan')
    products = category.product_set.all()
    context = {'products': products}

    return render(request, 'shop/proteins-page.html', context)

class ProductDetailView(DetailView):
    model = Product

def checkout(request):
    return render(request, 'shop/checkout.html')

def payment(request):
    cart = Cart.objects.get(user=request.user)
    total_price = cart.get_total_price()
    return render(request, 'shop/payment.html', {'total_price': total_price})

def thanks(request):
    return render(request, 'shop/thanks.html')

def about_us(request):
    return render(request, 'shop/aboutus.html')

def contact(request):
    return render(request, 'shop/contact.html')

######CART########
def cart_view(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cart_items.all()
    total_price = cart.get_total_price()

    return render(request, 'shop/cart_add.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = cart.cart_items.get_or_create(product=product)

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

def remove_from_cart(request, cart_item_id):
    cart = get_object_or_404(CartItem, id=cart_item_id)
    cart.delete()
    return redirect('cart')

def update_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 0))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()

    return redirect('cart')