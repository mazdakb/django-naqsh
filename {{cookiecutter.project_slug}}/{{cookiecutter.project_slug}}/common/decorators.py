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


class mute_signals(object):
    """Temporarily disables and then restores any django signals.

    Args:
        *signals (django.dispatch.dispatcher.Signal): any django signals

    Examples:
        with mute_signals(pre_init):
            user = UserFactory.build()
            ...

        @mute_signals(pre_save, post_save)
        class UserFactory(factory.Factory):
            ...

        @mute_signals(post_save)
        def generate_users():
            UserFactory.create_batch(10)
    """

    def __init__(self, *signals):
        self.signals = signals
        self.paused: dict = dict()

    def __enter__(self):
        for signal in self.signals:
            logger.debug('mute_signals: Disabling signal handlers %r',
                         signal.receivers)

            # Note that we're using implementation details of
            # django.signals, since arguments to signal.connect()
            # are lost in signal.receivers
            self.paused[signal] = signal.receivers
            signal.receivers = []

    def __exit__(self, exc_type, exc_value, traceback):
        for signal, receivers in self.paused.items():
            logger.debug('mute_signals: Restoring signal handlers %r',
                         receivers)

            signal.receivers = receivers
            with signal.lock:
                # Django uses some caching for its signals.
                # Since we're bypassing signal.connect and signal.disconnect,
                # we have to keep messing with django's internals.
                signal.sender_receivers_cache.clear()
        self.paused = {}

    def copy(self):
        return mute_signals(*self.signals)

    def __call__(self, callable_obj):
        @functools.wraps(callable_obj)
        def wrapper(*args, **kwargs):
            # A mute_signals() object is not re-entrant; use a copy every time.
            with self.copy():
                return callable_obj(*args, **kwargs)

        return wrapper
