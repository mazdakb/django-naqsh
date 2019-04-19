import secrets
import binascii
from datetime import timedelta

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings
from django.db import models

from Crypto.Hash import SHA512

from {{cookiecutter.project_slug}}.common.models import ActivatedModel, UniversalModel, TimestampedModel


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
        # prepare cryptographic ingredients
        full_token = secrets.token_hex(int(self.config.TOKEN_CHARACTER_LENGTH / 2))
        salt = secrets.token_hex(int(self.config.TOKEN_SALT_LENGTH / 2))
        digest = self.hash_token(full_token, salt)
        # set the expiry
        expires = timezone.now() + timedelta(seconds=self.config.TOKEN_TTL) if self.config.TOKEN_TTL != 0 else None
        # create the object
        auth_token = super(AuthTokenManager, self).create(
            digest=digest,
            key=self.get_key(full_token),
            salt=salt,
            user=user,
            expires=expires
        )
        # return token alongside AuthToken instance
        return auth_token, full_token


class AuthToken(UniversalModel, TimestampedModel):  # type: ignore
    user = models.ForeignKey('User', related_name='tokens', on_delete=models.CASCADE)
    digest = models.CharField(_('digest'), max_length=255)
    key = models.CharField(_('key'), max_length=255, unique=True)
    salt = models.CharField(_('salt'), max_length=255, unique=True)
    expires = models.DateTimeField(null=True, blank=True, db_index=True)

    objects = AuthTokenManager()

    class Meta:
        verbose_name = _('auth token')
        verbose_name_plural = _('auth tokens')
        ordering = ['-created']

    @property
    def is_expired(self):
        return self.expires < timezone.now()


class Session(UniversalModel, TimestampedModel, ActivatedModel):  # type: ignore
    user = models.ForeignKey(
        to='accounts.User',
        verbose_name=_('user'),
        related_name='sessions',
        on_delete=models.CASCADE
    )
    auth_token = models.OneToOneField(
        to=AuthToken,
        verbose_name=_('auth token'),
        related_name='session',
        editable=False,
        on_delete=models.CASCADE
    )
    user_agent = models.TextField(
        verbose_name=_('user agent'),
        editable=False,
        help_text=_('User-Agent of session with which user has logged in.')
    )
    ip_address = models.GenericIPAddressField(
        verbose_name=_('ip address'),
        blank=True,
        null=True,
        help_text=_('IP address of client. Web servers and proxies are ignored as best as possible.')
    )
    meta = JSONField(
        verbose_name=_('meta'),
        blank=True,
        null=True,
        help_text=_('Miscellaneous information related to this session.')
    )

    class Meta:
        verbose_name = _('session')
        verbose_name_plural = _('sessions')
        ordering = ['-created']

    @property
    def is_expired(self):
        return self.auth_token.is_expired


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


class User(AbstractUser, UniversalModel):  # type: ignore
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
