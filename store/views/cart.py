from django.shortcuts import render,redirect
from django.views import View
from store.Models.product import Product


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        if not ids:
            request.session['cart'] = {}
            return render(request, 'cart.html')
        else:
            products = Product.get_products_by_id(ids)
            print(products)
            return render(request, 'cart.html', {'products': products})

        request.session.get('cart').keys().clear()

