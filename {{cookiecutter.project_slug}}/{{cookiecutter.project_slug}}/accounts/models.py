import os
import uuid
import secrets
import binascii
from datetime import timedelta

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings
from django.db import models

from djchoices import DjangoChoices, ChoiceItem
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from versatileimagefield.fields import VersatileImageField
from phonenumbers import parse, is_valid_number, format_number, PhoneNumberFormat, NumberParseException

from {{cookiecutter.project_slug}}.common.models import UniversalModel, TimestampedModel
from {{cookiecutter.project_slug}}.common.storages import path_for_object, replace_file_name


def accounts_profile_path(instance, filename):
    return os.path.join(path_for_object(instance), replace_file_name(filename, 'picture'))


class AuthTokenConfig(object):
    TOKEN_CHARACTER_LENGTH = 64
    TOKEN_DIGEST_LENGTH = 128
    TOKEN_SALT_LENGTH = 16
    TOKEN_TTL = 0

    def __init__(self):
        for prop, value in getattr(settings, 'AUTH_TOKEN', {}).items():
            setattr(self, 'token_{}'.format(prop.lower()), value)


class AuthTokenManager(models.Manager):
    config = AuthTokenConfig()

    def get_key(self, token):
        return token[:int(self.config.TOKEN_CHARACTER_LENGTH / 2)]

    def hash_token(self, token, salt):
        digest = hashes.Hash(hashes.SHA512(), backend=default_backend())
        digest.update(binascii.unhexlify(token))
        digest.update(binascii.unhexlify(salt))
        return binascii.hexlify(digest.finalize()).decode()

    def create(self, user):
        token = secrets.token_hex(int(self.config.TOKEN_CHARACTER_LENGTH / 2))
        salt = secrets.token_hex(int(self.config.TOKEN_SALT_LENGTH / 2))
        digest = self.hash_token(token, salt)

        expires = None
        if self.config.TOKEN_TTL != 0:
            expires = timezone.now() + timedelta(seconds=self.config.TOKEN_TTL)

        super(AuthTokenManager, self).create(
            digest=digest,
            key=self.get_key(token),
            salt=salt,
            user=user,
            expires=expires
        )
        # Note only the token string - not the AuthToken object - is returned
        return token


class AuthToken(UniversalModel, TimestampedModel):
    digest = models.CharField(_('digest'), max_length=255)
    key = models.CharField(_('key'), max_length=255, db_index=True)
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


def phone_validator(value):
    # prepend + at the beginning
    value = '+{}'.format(value)
    # parse the number
    try:
        number = parse(value, None)
    except NumberParseException:
        raise ValidationError(
            _('%(value)s is not a valid phone number'),
            params={'value': value[1:]},
        )
    if not is_valid_number(number):
        raise ValidationError(
            _('%(value)s is not a valid Iranian phone number'),
            params={'value': value[1:]},
        )


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):
        """
        Create and save a user with the given phone, and password.
        """
        if not phone:
            raise ValueError('The given phone must be set')
        email = self.normalize_email(extra_fields.pop('email', ''))
        user = self.model(phone=phone, email=email, **extra_fields)
        user.set_password(password) if password is not None else user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            'unique': _("A user with smake email address already exists."),
        },
    )
    phone = models.CharField(
        _('phone'),
        max_length=15,
        validators=[phone_validator],
        blank=True,
        db_index=True,
        help_text=_('Valid phone number in E.164 international form'),
    )

    username = None  # overwritten to remove the `username` field from model

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return format_number(
            parse('+{}'.format(self.phone)),
            PhoneNumberFormat.INTERNATIONAL
        )[1:]  # phone number formatting without leading zero


class ProfileGenders(DjangoChoices):
    MALE = ChoiceItem('MALE', _('MALE'))
    FEMALE = ChoiceItem('FEMALE', _('FEMALE'))


class Profile(UniversalModel, TimestampedModel):
    user = models.OneToOneField(
        User,
        verbose_name=_('user'),
        related_name='profile',
        on_delete=models.CASCADE
    )
    gender = models.CharField(
        _('gender'),
        max_length=6,
        default=ProfileGenders.MALE,
        choices=ProfileGenders.choices,
        validators=[ProfileGenders.validator],
        help_text=_('designates the gender of user'),
    )
    birthdate = models.DateField(_('birthdate'), null=True, blank=True)
    picture = VersatileImageField(_('picture'), blank=True, upload_to=accounts_profile_path)

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    def __str__(self):
        return str(self.id)
