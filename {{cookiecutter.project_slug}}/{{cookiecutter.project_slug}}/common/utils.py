import re
import secrets
from typing import Union

import inflection

from django.utils.translation import ugettext_lazy as _


def round_to_half_k(value: Union[int, float]) -> int:
    """Round to half a thousand

    Round the given value to nearest half a thousand.

    Notes:
        - This function is commonly used in calculating monetary values.

    :param value:
    :return:
    """
    return round(value / 500) * 500


def to_naive_phone(phone: str):
    """Get naive phone number

    Convert international phone number to naive form.
    For example 989123214498 becomes 09123214498.

    :param phone:
    :return:
    """
    if phone.isdigit():
        return f'0{phone[2:]}'
    else:
        raise ValueError(_(f'{phone} is not a valid national phone number'))


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


def normalize_slug(slug: str) -> str:
    """Normalize slug string

    Get the slug to a normal form
    by removing non-word characters and
    replacing space(s) with an underscore.

    :param slug:
    :return:
    """
    # strip the slug of extra white spaces
    slug = slug.strip()
    # process slug using inflection library
    slug = inflection.underscore(slug)
    # Remove all non-word characters (everything except numbers and letters)
    slug = re.sub(r"[^\w\s]", "", slug)
    # Replace all runs of whitespace with a single underscore
    slug = re.sub(r"\s+", "_", slug)
    # convert slug to characters to lowercase
    slug = slug.lower()
    # return the result
    return slug


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
