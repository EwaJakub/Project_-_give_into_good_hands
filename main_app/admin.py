from django.contrib import admin
from .models import Category, Donation, Institution

# Register your models here.

admin.site.register(Category)

admin.site.register(Donation)

admin.site.register(Institution)