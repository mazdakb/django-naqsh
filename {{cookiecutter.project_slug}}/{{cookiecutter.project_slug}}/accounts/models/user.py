from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from {{ cookiecutter.project_slug }}.accounts.managers import UserManager
from {{ cookiecutter.project_slug }}.common.models import UniversalModelMixin, ActivatedModelMixin


class User(AbstractUser, UniversalModelMixin, ActivatedModelMixin):
    email = models.EmailField(
        verbose_name=_("email address"),
        max_length=255,
        unique=True,
        error_messages={"unique": _("A user with this email address already exists.")},
    )
    is_verified = models.BooleanField(
        verbose_name=_("email verified"),
        default=False,
        help_text=_("Designates if this user's email has been verified."),
    )

    # overwritten to remove the useless `username` field from database
    username = None  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects: UserManager = UserManager()  # type: ignore

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ["-date_joined"]

    def __str__(self) -> str:
        return self.email
