import secrets
import binascii
from datetime import timedelta

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings
from django.db import models

from Crypto.Hash import SHA512

from {{cookiecutter.project_slug}}.common.models import UniversalModel, TimestampedModel


class AuthTokenConfig(object):
    TOKEN_CHARACTER_LENGTH = 64
    TOKEN_SALT_LENGTH = 16
    TOKEN_TTL = 0

    def __init__(self):
        for prop, value in getattr(settings, 'AUTH_TOKEN', {}).items():
            setattr(self, f'TOKEN_{prop}', value)


class AuthTokenManager(models.Manager):
    config = AuthTokenConfig()

    def get_key(self, token):
        return token[:int(self.config.TOKEN_CHARACTER_LENGTH / 2)]

    def hash_token(self, token, salt):
        hash_object = SHA512.new()
        hash_object.update(binascii.unhexlify(token))
        hash_object.update(binascii.unhexlify(salt))
        return hash_object.hexdigest()

    def create(self, user):
        token = secrets.token_hex(int(self.config.TOKEN_CHARACTER_LENGTH))
        salt = secrets.token_hex(int(self.config.TOKEN_SALT_LENGTH / 2))
        digest = self.hash_token(token, salt)

        expires = None
        if self.config.TOKEN_TTL != 0:
            expires = timezone.now() + timedelta(seconds=self.config.TOKEN_TTL)

        authtoken = super(AuthTokenManager, self).create(
            digest=digest,
            key=self.get_key(token),
            salt=salt,
            user=user,
            expires=expires
        )
        # return token alongside authtoken instance
        return authtoken, token


class AuthToken(UniversalModel, TimestampedModel):
    digest = models.CharField(_('digest'), max_length=255)
    key = models.CharField(_('key'), max_length=255, unique=True)
    salt = models.CharField(_('salt'), max_length=255, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tokens', on_delete=models.CASCADE)
    expires = models.DateTimeField(null=True, blank=True, db_index=True)

    objects = AuthTokenManager()

    class Meta:
        verbose_name = _('auth token')
        verbose_name_plural = _('auth tokens')
        ordering = ['-created']

    @property
    def is_expired(self):
        return self.expires < timezone.now()


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password) if password is not None else user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser, UniversalModel):
    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            'unique': _('A user with make email address already exists.'),
        },
    )

    username = None  # overwritten to remove the useless `username` field from database

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email
