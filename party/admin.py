from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Party, Gift, Guest

# User model
@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    pass

# Party model
@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid",)

# Gifts model
@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid",)

# Guests model
@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid",)