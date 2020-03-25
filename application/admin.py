from django.contrib import admin
from .models import Customer,Product,Order,Tag


class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "name","phone","email","data_created"
    ]

admin.site.register(Customer,CustomerAdmin,)

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name","price","category","data_created"
    ]

admin.site.register(Product,ProductAdmin,)

class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "data_created","status","Customer","Product"
    ]

admin.site.register(Order,OrderAdmin,)

admin.site.register(Tag)