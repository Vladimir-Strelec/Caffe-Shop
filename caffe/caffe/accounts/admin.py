from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from caffe.accounts.models import Profile, ShopUser


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(ShopUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_superuser', 'is_staff')

