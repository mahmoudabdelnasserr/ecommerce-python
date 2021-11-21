
from django.urls import path
from . import views


urlpatterns = [
        path('', views.wishlist, name='wishlist'),
        path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
        path('remove_wishlist_item/<int:product_id>/<int:wishlist_item_id>/', views.remove_wishlist_item, name='remove_wishlist_item'),
  ]