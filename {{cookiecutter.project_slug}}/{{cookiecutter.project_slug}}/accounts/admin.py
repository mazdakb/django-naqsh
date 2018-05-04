from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

from .models import AuthToken, User, Profile


class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no password, from the given email.
    """
    class Meta:
        model = User
        fields = ['phone', 'email']


class AuthTokenAdmin(admin.StackedInline):
    model = AuthToken
    fields = ['pk', 'digest', 'key', 'salt', 'user', 'expires']
    readonly_fields = fields
    max_num = 0
    {% if cookiecutter.use_grappelli == "y" -%}
    classes = ['grp-collapse grp-open']
    inline_classes = ['grp-collapse grp-open']
    {%- endif %}


class ProfileInlineAdmin(admin.StackedInline):
    model = Profile
    fields = ['gender', 'birthdate', 'picture']
    readonly_fields = ['created', 'updated']
    {% if cookiecutter.use_grappelli == "y" -%}
    classes = ['grp-collapse grp-open']
    inline_classes = ['grp-collapse grp-open']
    {%- endif %}


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    fieldsets = [
        (None, {'fields': ['id', 'phone', 'email', 'password']}),
        (_('personal info'), {'fields': ['first_name', 'last_name']}),
        (_('permissions'), {'fields': ['is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions']}),
        (_('important dates'), {'fields': ['last_login', 'date_joined']}),
    ]
    add_fieldsets = [
        (None, {
            'classes': ('wide',),
            'fields': ['phone', 'email', 'first_name', 'last_name', 'password1', 'password2'],
        }),
    ]
    readonly_fields = ['id', 'last_login', 'date_joined']
    list_display = ['national_formatted_phone', 'full_name', 'email', 'date_joined']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'date_joined', 'groups']
    search_fields = ['id', 'phone', 'first_name', 'last_name', 'email']
    ordering = ['-date_joined']
    filter_horizontal = ['groups', 'user_permissions']
    inlines = [ProfileInlineAdmin, AuthTokenAdmin]

    def full_name(self, obj: User):
        return obj.get_full_name()

    def national_formatted_phone(self, obj: User):
        return str(obj)
