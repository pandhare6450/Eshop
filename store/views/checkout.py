from django.shortcuts import redirect
from django.views import View
from store.Models.product import Product
from store.Models.orders import Order
from store.Models.customer import Customer


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(product=product,
                          customer=Customer(id=customer),
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
            request.session['cart'] = {}
        return redirect('cart')
