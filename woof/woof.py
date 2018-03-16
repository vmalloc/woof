from .backends import telegram_backend # pylint: disable=unused-import

from .backends.base import BACKENDS


def notify(message):
    """Sends the specified message through available backends
    """
    for backend_class in BACKENDS:
        backend = backend_class.try_configure()
        if backend is not None:
            backend.notify(message)
