from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Client, Order1, OrderStruct, Goods, Delivery, Storage, User

# Register your models here.

admin.site.register(Client)
admin.site.register(Order1)
admin.site.register(OrderStruct)
admin.site.register(Goods)
admin.site.register(Delivery)
admin.site.register(Storage)
admin.site.register(User)