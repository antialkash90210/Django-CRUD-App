from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Item


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('mobile_number', 'address')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

# Register the Item model
admin.site.register(Item)
