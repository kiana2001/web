from django.contrib import admin
from .models import User

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class UserAdmin(BaseUserAdmin):
    # Specify the fields to be displayed in the user change list
    list_display = ('email', 'first_name', 'last_name', 'is_staff')

    # Specify the fields to be displayed in the user creation/edit form
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number', 'ssn')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
    )

    # Specify the fields to be displayed readonly in the user change form
    readonly_fields = ('email',)

    # Specify the filter options
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

    # Specify the search fields
    search_fields = ('email', 'first_name', 'last_name')

    # Specify the ordering of the users
    ordering = ('email',)

    # Specify the actions for the selected users
    actions = ['make_staff', 'remove_staff']

    def make_staff(self, request, queryset):
        # Custom action to make selected users staff members
        queryset.update(is_staff=True)

    make_staff.short_description = "Make selected users staff"

    def remove_staff(self, request, queryset):
        # Custom action to remove staff status from selected users
        queryset.update(is_staff=False)

    remove_staff.short_description = "Remove staff status from selected users"

admin.site.register(User, UserAdmin)