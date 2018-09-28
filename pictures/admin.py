from django.contrib import admin
from .models import Picture,Location,Category

# Register your models here.
admin.site.register(Picture)
admin.site.register(Category)
admin.site.register(Location)
