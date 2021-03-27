from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.users.models import BaseUser


# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = ("email", "company_name", "created_time", "last_login", "is_admin", "is_active", "is_staff")
    search_fields = ("email", "company_name")
    readonly_fields = ("created_time", "last_login")

    filter_horizontal = ()
    ordering = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = [
        (None, {
            'classes': 'wide',
            'fields': ('email', 'company_name', 'phone', 'password')
        })
    ]


admin.site.register(BaseUser, UserAdmin)

# email
# company_name
# phone
# created_time
# last_login
# is_admin
# is_active
# is_staff
# is_superuser
