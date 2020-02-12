from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from {{ cookiecutter.project_slug }}.common.models import (
    ActivatedModelMixin,
    UniversalModelMixin,
    TimestampedModelMixin,
)


class Session(UniversalModelMixin, TimestampedModelMixin, ActivatedModelMixin):
    """Session data model

    This class holds the session data for a single user
    which could be used to authenticate and identify a request
    to the {{ cookiecutter.project_name }}.
    """

    user = models.ForeignKey(
        to="accounts.User",
        verbose_name=_("user"),
        related_name="sessions",
        on_delete=models.CASCADE,
    )
    digest = models.CharField(verbose_name=_("digest"), max_length=255)
    key = models.CharField(verbose_name=_("key"), max_length=255, unique=True)
    salt = models.CharField(verbose_name=_("salt"), max_length=255, unique=True)
    expires = models.DateTimeField(
        verbose_name=_("expires at"), null=True, blank=True, db_index=True
    )
    user_agent = models.TextField(
        verbose_name=_("user agent"),
        editable=False,
        help_text=_("User-Agent of session with which user has logged in."),
    )
    ip_address = models.GenericIPAddressField(
        verbose_name=_("ip address"),
        blank=True,
        null=True,
        help_text=_(
            "IP address of client. Web servers and proxies are ignored as best as possible."
        ),
    )

    class Meta:
        verbose_name = _("session")
        verbose_name_plural = _("sessions")
        ordering = ["-created"]

    @property
    def is_expired(self) -> bool:
        return self.expires < timezone.now() if self.expires else False
