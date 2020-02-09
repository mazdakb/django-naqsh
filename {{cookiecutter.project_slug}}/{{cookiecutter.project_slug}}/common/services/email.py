from typing import Iterable, Optional

{% if cookiecutter.use_drf != 'y' -%}
from django.core.mail import EmailMessage
{% endif -%}

import attr

from marketplace.common.enums import EmailTemplate
from marketplace.common.tasks import send_transactional_email

from .abstract import Service


@attr.s(auto_attribs=True)
class EmailService(Service):
    """Email service

    TODO: provide global email context

    A service used to orchestrate and send emails
    """

    _GLOBAL_CONTEXT: dict = attr.ib(
        factory=dict
    )  # Global email context i.e banners, etc.

    def initiate_transactional_email(
        self,
        template: EmailTemplate,
        recipients: Iterable[str],
        context: dict,
        subject: Optional[str] = None,
        body: Optional[str] = None,
    ):
        """Initiate sending transactional email

        Send a transactional email with a template id and context to
        the designated recipients incorporating django-anymail's ESP templates.

        Notes:
            - The method used to send emails works with anymail but also
              plays well with local project setup and all configurations (i.e mailhog)
              by using Django's email backend.

        :param template:
        :param recipients:
        :param context:
        :param subject:
        :param body:
        :return:
        """
        {% if cookiecutter.use_drf == 'y' -%}
        send_transactional_email.delay(
            template=template,
            recipients=recipients,
            context=context,
            global_context=self._GLOBAL_CONTEXT,
            subject=subject,
            body=body,
        )
        {% else %}
        message = EmailMessage(to=list(recipients), subject=subject or "", body=body or "")
        message.template_id = template
        message.merge_data = context
        message.merge_data_global = global_context if global_context else {}
        message.send()
        {%- endif %}
