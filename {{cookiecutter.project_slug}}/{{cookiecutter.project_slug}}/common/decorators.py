import logging
import functools

from django.db import transaction

logger = logging.getLogger(__name__)


def after_transaction(func):
    """After successful transaction

    Execute a function only after a transaction is completed.

    Notes:
        If the transaction.on_commit() gets executed while not in an active transaction, it will run right away.

    :param func:
    :return:
    """

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        return transaction.on_commit(lambda: func(*args, **kwargs))

    return wrapped
