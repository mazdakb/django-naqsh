import secrets

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
