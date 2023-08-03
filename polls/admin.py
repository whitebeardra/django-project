from django.contrib import admin
from .models import Post, shopping_item

class shoitem(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount')


admin.site.register(Post)
admin.site.register(shopping_item, shoitem)
