from typing import Optional

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

from {{ cookiecutter.project_slug }}.common.models import ActivatedModelManager

from {{ cookiecutter.project_slug }}.common.models import UniversalModelMixin


class UserManager(BaseUserManager, ActivatedModelManager):
    use_in_migrations = True

    def _create_user(
        self, email: str, password: Optional[str], **extra_fields
    ) -> "User":
        """
        Create and save a user with the given email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password) if password else user.set_unusable_password()
        user.save(using=self._db)  # type: ignore
        return user

    def create_user(self, email: str, password: str = None, **extra_fields) -> "User":
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email: str, password: str, **extra_fields) -> "User":
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser, UniversalModelMixin):
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
