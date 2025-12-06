from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    # Show email, username, staff status (removed full_name)
    list_display = ('email', 'username', 'is_staff')
    ordering = ('email',)

    # Removed full_name method since you don’t want to show full name

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('username',)}),  # only username here, removed first_name, last_name
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

    search_fields = ('email', 'username')  # removed first_name and last_name from search
