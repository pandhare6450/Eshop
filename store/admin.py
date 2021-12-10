from django.contrib import admin
from .Models.product import Product
from .Models.Category import Category
from .Models.customer import Customer
from .Models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name','Category','price']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)