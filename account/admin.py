from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser




class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets  # Use the default UserAdmin fieldsets
    add_fieldsets = UserAdmin.add_fieldsets  # Use the default add_fieldsets
    
admin.site.register(CustomUser, CustomUserAdmin)
