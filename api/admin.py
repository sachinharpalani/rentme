from django.contrib import admin

from .models import Category,Customer,Item

# Register your models here.

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Item)
