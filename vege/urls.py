from django.urls import path
from .import views
from .views import(
    CheckoutView,
OrderSummaryView,
PaymentView,
AddCouponView)
urlpatterns = [
    path("index",views.index,name="index"),
    path("about",views.about),
    path("blogsingle",views.blogsingle),
    path("blog",views.blog),
    path("cart",views.cart,name="cart"),
    path("cart",OrderSummaryView.as_view(),name="cart"),
    path("update_cart/<id>",views.update_cart,name="update_cart"),
    path("remove_from_cart/<id>",views.remove_from_cart,name="remove_from_cart"),
    path("remove_single_product_from_cart/<id>",views.remove_single_product_from_cart,name="remove_single_product_from_cart"),
   
    path("checkout",CheckoutView.as_view(), name="checkout"),
    path("payment/<payment_option>/",PaymentView.as_view(), name="payment"),
    path("add_coupon",AddCouponView.as_view(), name="add_coupon"),
    path("contact",views.contact),
    path("productsingle",views.productsingle),
    path("shop",views.shop),
    path("wishlist",views.wishlist), 
    path("wishlist_store/<id>",views.wishlist_store,name="wishlist_store"),
    
    ]
