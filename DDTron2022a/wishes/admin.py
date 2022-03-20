from django.contrib import admin
from .models import Wish

# Register your models here.


class WishAdmin(admin.ModelAdmin):
    model = Wish
    list_display = ['wish_text','author', 'event','assigned_to', 'id']    


admin.site.register(Wish,WishAdmin)