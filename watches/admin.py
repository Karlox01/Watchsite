from django.contrib import admin

from .models import Category, Item, Offer

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Offer)

