import secrets
import binascii
from typing import Union, Tuple

from django.db.models import Q
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

from {{ cookiecutter.project_slug }}.accounts.models import Session, User


class BearerTokenAuthentication(TokenAuthentication):
    """
    Simple token based authentication.

    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Bearer ".  For example:

        Authorization: Bearer 401f7ac837da42b97f613d789819ff93537bee6a
    """

    keyword = "Bearer"
    model = Session

    def authenticate_credentials(self, token: str) -> Union[None, Tuple[User, Session]]:
        """Authenticate user credentials

        # TODO: fix token hashing to use SessionService

        Notes:
            - for more information take a look at
              https://www.django-rest-framework.org/api-guide/authentication/#custom-authentication

        :param token: user provided full token for authentication
        :return: None if user could not be authenticated and a
                 tuple of User and stored_token if authenticated successfully
        """
        model = self.get_model()
        msg = _("Invalid token.")

        stored_sessions = model.objects.filter(
            Q(key=model.objects.get_key(token))
            & (Q(expires__isnull=True) | Q(expires__gt=timezone.now()))
        ).select_related("user")

        if not stored_sessions.exists():
            raise exceptions.AuthenticationFailed(msg)

        if not stored_sessions.first().user.is_active:
            raise exceptions.AuthenticationFailed(_("This user is deactivated!"))

        for session in stored_sessions.actives():
            try:
                digest = model.objects.hash_token(token, session.salt)
            except (TypeError, binascii.Error):
                raise exceptions.AuthenticationFailed(msg)
            if secrets.compare_digest(digest, session.digest):
                return session.user, session

        raise exceptions.AuthenticationFailed(msg)
