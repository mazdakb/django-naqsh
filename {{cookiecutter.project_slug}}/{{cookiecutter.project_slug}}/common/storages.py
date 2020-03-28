import os
import secrets

from django.conf import settings
from django.core.files.storage import FileSystemStorage

import inflection
{% if cookiecutter.cloud_provider == 'AWS' -%}
from storages.backends.s3boto3 import S3Boto3Storage
{%- endif %}

secret_random = secrets.SystemRandom()


{% if cookiecutter.cloud_provider == 'AWS' -%}
class StaticRootS3Boto3Storage(S3Boto3Storage):
    location = "static"
    default_acl = "public-read"


class MediaRootS3Boto3Storage(S3Boto3Storage):
    location = "media"
    file_overwrite = False
{%- elif cookiecutter.cloud_provider == 'GCP' -%}
from storages.backends.gcloud import GoogleCloudStorage


class StaticRootGoogleCloudStorage(GoogleCloudStorage):
    location = "static"
    default_acl = "publicRead"


class MediaRootGoogleCloudStorage(GoogleCloudStorage):
    location = "media"
    file_overwrite = False
{%- endif %}


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        """Returns a filename that's free on the target storage system, and
        available for new content to be written to.

        Found at http://djangosnippets.org/snippets/976/

        Notes:
            This file storage solves overwrite on upload problem.
        """
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


def random_file_name(filename: str) -> str:
    """
    Replace file name with a random string and preserving its extension.
    Result would look like <random_string>.<extension>

    :param filename: str
    :return: str
    """
    return f'{secrets.token_urlsafe(16)}.{filename.split(".")[-1]}'


def replace_file_name(filename: str, replace_with: str) -> str:
    """
    Replace file name with a fixed string and preserving its extension.
    Result would look like <replace_with>.<extension>

    :param filename: str
    :param replace_with: str
    :return: str
    """
    return f"{replace_with}.{filename.split('.')[-1]}"


def path_for_object(
    instance, get_object_name=lambda i: str(i.id), field_name: str = ""
) -> str:
    """
    Generate storage path for object.
    Result would look like <MEDIA_ROOT>/<app_label>/<model>/<str(instance)>/<field>/<filename>

    :param instance:
    :param get_object_name:
    :param field_name:
    :return:
    """
    # extract app label using instance's meta
    app_label = instance._meta.app_label
    # get instance class name
    class_name = inflection.pluralize(instance.__class__.__name__.lower())
    # use provided function to get a string representation suitable for storage
    object_name = get_object_name(instance)
    # get get field name and pluralize it
    field_name = inflection.pluralize(field_name if field_name else "")
    # combine values
    return os.path.join(app_label, class_name, object_name, field_name)
