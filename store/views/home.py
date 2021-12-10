from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.Models.product import Product
from store.Models.Category import Category
from django.views import View
from django.core.paginator import Paginator

class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity :
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart', cart)
        return redirect('homepage')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        category_ID = request.GET.get('category')

        if category_ID:
            products = Product.get_all_products_by_categoryid(category_ID)
        else:
            products = Product.get_all_products()

        data = {}
        data['products'] = products
        data['categories'] = categories
        p = Paginator(products, 6)

        if not category_ID:
            page_number = request.GET.get('category?page')
        else:
            page_number = request.GET.get('category?page')
        page_obj = p.get_page(page_number)
        return render(request,'index.html',{'page_obj':page_obj,'categories':categories})


def okay():
    return HttpResponse('pretend-binary-data-here', content_type='image/jpeg')
