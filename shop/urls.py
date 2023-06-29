from django.urls import path
from .views import (landing_page, contact, menu_page,
                    proteins_page, equipment_page, suplements,
                     workout_plans, ProductDetailView,
                    checkout, payment, thanks, about_us,
                    cart_view, add_to_cart, remove_from_cart,
                    update_cart)

urlpatterns = [
    path('', landing_page, name='landing-page'),
    path('menu/', menu_page, name='menu-page'),
    path('menu/protein/', proteins_page, name='protein-page'),
    path('menu/equipment/', equipment_page, name='equipments-page'),
    path('menu/supplements/', suplements, name='supplements-page'),
    path('menu/workoutplans/', workout_plans, name='workout-plan-page'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('checkout/', checkout, name='checkout'),
    path('payment/', payment, name='payment'),
    path('thanks/', thanks, name='thanks'),
    path('aboutus/', about_us, name='about_us'),
    path('contact/', contact, name='contact'),
    ########CART#############
    path('cart/', cart_view, name='cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:cart_item_id>/', update_cart, name='update_cart'),
]