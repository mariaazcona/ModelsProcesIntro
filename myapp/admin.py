from django.contrib import admin
from .models import Item, Purchase, Review

# Register your models here.
admin.site.register(Purchase)
admin.site.register(Item)
admin.site.register(Review)