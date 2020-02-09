from typing import Iterable, Optional

from django.core.mail import EmailMessage

from celery import shared_task

from {{ cookiecutter.project_slug }}.common.enums import EmailTemplate


@shared_task(name="common.email.send_transactional_email")
def send_transactional_email(
    template: EmailTemplate,
    recipients: Iterable[str],
    context: dict,
    global_context: Optional[dict] = None,
    subject: Optional[str] = None,
    body: Optional[str] = None,
):
    """Send transactional email asynchronously

    Send a transactional email with a template id and context to
    the designated recipients incorporating django-anymail's ESP templates.

    Notes:
        - The method used to send emails works with anymail but also
          plays well with local project setup and all configurations (i.e mailhog)
          by using Django's email backend.

    :param template:
    :param recipients:
    :param context:
    :param global_context:
    :param subject:
    :param body:
    :return:
    """
    message = EmailMessage(to=list(recipients), subject=subject or "", body=body or "")
    message.template_id = template
    message.merge_data = context
    message.merge_data_global = global_context if global_context else {}
    message.send()
