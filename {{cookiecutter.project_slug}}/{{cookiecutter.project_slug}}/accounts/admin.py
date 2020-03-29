from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from {{ cookiecutter.project_slug }}.accounts.models import User


class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no password, from the given email.
    """

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    fieldsets = [
        (None, {"fields": ["id", "email", "password"]}),
        (_("Personal Info"), {"fields": ["first_name", "last_name"]}),
        (
            _("Permissions"),
            {
                "fields": [
                    "is_active",
                    "is_verified",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ]
            },
        ),
        (_("Important Dates"), {"fields": ["last_login", "date_joined"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ("wide",),
                "fields": [
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                ],
            },
        )
    ]
    readonly_fields = ["id", "last_login", "date_joined"]
    list_display = ["full_name", "email", "date_joined"]
    list_filter = ["is_staff", "is_superuser", "is_active", "date_joined", "groups"]
    search_fields = ["id", "first_name", "last_name", "email"]
    ordering = ["-date_joined"]
    filter_horizontal = ["groups", "user_permissions"]

    def full_name(self, obj: User):
        return obj.get_full_name()
