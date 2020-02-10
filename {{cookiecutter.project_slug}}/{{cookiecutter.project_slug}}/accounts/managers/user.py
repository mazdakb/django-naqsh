from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from django.contrib.auth.base_user import BaseUserManager

from {{ cookiecutter.project_slug }}.common.models import ActivatedModelManager

if TYPE_CHECKING:
    from {{ cookiecutter.project_slug }}.accounts.models import User


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
        user.save(using=self._db)
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
