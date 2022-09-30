from django.contrib import admin

# Register your models here.

from .models import Product
#todo NOTES: register the app in admin site
admin.site.register(Product)
