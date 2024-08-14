from django.contrib import admin

# Register your models here.
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    # Define the forms and fields to display in the admin interface
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'is_company_admin', 'is_client_customer', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_company_admin', 'is_client_customer'),
        }),
    )
    
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_company_admin', 'is_client_customer', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

# Register the custom User model with the CustomUserAdmin class
admin.site.register(User, CustomUserAdmin)
