from django.shortcuts import render, get_object_or_404, redirect
from carts.views import _cart_id
from store.models import Product

from wishlists.models import WishlistItem, Wishlist

from django.core.exceptions import ObjectDoesNotExist
def _wish_id(request):
    wishlist = request.session.session_key
    if not wishlist:
        wishlist = request.session.create()
    return wishlist

def wishlist(request, wishlist_id=None, wishlist_items=None):
    try:
        if request.user.is_authenticated:
            wishlist_items = WishlistItem.objects.filter(user=request.user)
        else:
            wishlist = Wishlist.objects.get(wishlist_id=wishlist_id)
            wishlist_items = WishlistItem.objects.filter(wishlist=wishlist)
    except ObjectDoesNotExist:
        pass #just ignore

    context = {
        'wishlist_items': wishlist_items,

    }
    return render(request, 'wish.html', context)

def remove_wishlist_item(request, product_id, wishlist_item_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user.is_authenticated:
        wishlist_item = WishlistItem.objects.get(product=product, user=request.user, id=wishlist_item_id)
        print(wishlist_item.id)
    else:
        wishlist = Wishlist.objects.get(cart_id=_cart_id(request))
        wishlist_item = WishlistItem.objects.get(product=product, wishlist=wishlist, id=wishlist_item_id)
        print(wishlist_item.id)
    wishlist_item.delete()
    return redirect('wishlist')

def add_to_wishlist(request, product_id):
    current_user = request.user
    if current_user.is_authenticated:
        product = Product.objects.get(id=product_id) #get the product
        try:
            wishlist = Wishlist.objects.get(wishlist_id=_wish_id(request))
        except:
            wishlist = Wishlist.objects.create(
                wishlist_id = _wish_id(request)
            )
        wishlist.save()

        try:
            wishlist_item = WishlistItem.objects.get(product=product, wishlist=wishlist, user=current_user)
            wishlist_item.user = current_user
            wishlist_item.save()
        except:
            wishlist_item = WishlistItem.objects.create(
                product = product,
                wishlist = wishlist,
                user = current_user,
            )
            wishlist_item.save()
    else:
        return redirect('login')
    return redirect('wishlist')



