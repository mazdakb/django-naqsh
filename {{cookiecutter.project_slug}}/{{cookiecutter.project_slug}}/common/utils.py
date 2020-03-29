import os
import secrets
from datetime import date
from typing import Callable, Optional

from django.db.models import Model

__all__ = ["generate_random_slug", "get_initial_words"]


def generate_random_slug(length: int = 10) -> str:
    """Generate random slug string

    Generate a url safe random alphanumeric string with specified length

    Notes:
        - Minimum slug length is 10. Because reducing the slug length
          leads to higher probability of collision.

    :param length:
    :return:
    """
    return secrets.token_hex(max(length, 10) // 2)


def get_initial_words(text: str, word_count: int = 10, append_dots: bool = True) -> str:
    """Get initial words

    Get the first `word_count` words of text if the it is long enough.
    A "..." will be appended to trimmed text by default which can be controlled
    by `append_dots` argument.

    :param text:
    :param word_count:
    :param append_dots:
    :return:
    """
    # split the text into words
    content_slices = text.split()
    # return the first few words if text is long enough
    trimmed_text = content_slices[:word_count]
    # prepare the initial string
    initial = " ".join(trimmed_text)
    # append dots if set
    return f"{initial}..." if append_dots else initial


def randomize_file_name(filename: str) -> str:
    """
    Append the file name with a random string, preserving its extension.
    Result would look like `<original_name>.<random_string>.<extension>`
    :param filename: str
    :return: str
    """
    name, file_extension = os.path.splitext(filename)
    return f"{name}.{secrets.token_hex(4)}.{file_extension[1:]}"


def replace_file_name(filename: str, replace_with: str) -> str:
    """
    Replace file name with a fixed string, preserving its extension.
    Result would look like `<replace_with>.<extension>`
    :param filename: str
    :param replace_with: str
    :return: str
    """
    _, file_extension = os.path.splitext(filename)
    return f"{replace_with}.{file_extension[1:]}"


def path_for_object(
    instance: Model,
    get_object_identifier: Optional[Callable[[Model], str]] = None,
    by_date: Optional[bool] = False,
) -> str:
    """
    Generate storage path for object.
    By default, Result would look like <MEDIA_ROOT>/<app_label>/<model>/<str(instance.pk)>/[date]/<filename>
    :param instance:
    :param get_object_identifier:
    :param by_date:
    :return:
    """
    # extract app label using instance's meta
    app_label = instance._meta.app_label.lower()
    # get instance class name
    class_name = instance.__class__.__name__.lower()
    # combine values
    return os.path.join(
        app_label,
        class_name,
        get_object_identifier(instance) if get_object_identifier else "",
        date.today().strftime("%Y-%m-%d") if by_date else "",
    )
