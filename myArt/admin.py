from django.contrib import admin
from .models import Owner,Location,Gallery,Category

# Register your models here.
admin.site.register(Owner)
admin.site.register(Location)
admin.site.register(Gallery)
admin.site.register(Category)
