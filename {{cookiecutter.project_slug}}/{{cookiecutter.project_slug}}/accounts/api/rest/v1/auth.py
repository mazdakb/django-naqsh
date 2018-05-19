import secrets
import binascii

from django.db.models import Q
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

from {{cookiecutter.project_slug}}.accounts.models import AuthToken


class BearerTokenAuthentication(TokenAuthentication):
    """
    Simple token based authentication.

    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Bearer ".  For example:

        Authorization: Bearer 401f7ac837da42b97f613d789819ff93537bee6a
    """
    keyword = 'Bearer'
    model = AuthToken

    def authenticate_credentials(self, token):
        model: AuthToken = self.get_model()
        msg = _('Invalid token.')

        stored_tokens = model.objects.filter(
            Q(key=model.objects.get_key(token)) &
            (Q(expires__isnull=True) | Q(expires__gt=timezone.now())) &
            Q(user__is_active=True),
        ).select_related('user')

        if not stored_tokens.exists():
            raise exceptions.AuthenticationFailed(msg)

        for stored_token in stored_tokens.all():
            try:
                digest = model.objects.hash_token(token, stored_token.salt)
            except (TypeError, binascii.Error):
                raise exceptions.AuthenticationFailed(msg)
            if secrets.compare_digest(digest, stored_token.digest):
                return stored_token.user, stored_token

        raise exceptions.AuthenticationFailed(msg)
