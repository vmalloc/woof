import os
import pytest

import woof.backends.base


@pytest.fixture
def custom_backend_class(request):
    class CustomBackend(woof.backends.base.Backend):

        messages = []

        def __init__(self, param1, param2):
            self.param1 = param1
            self.param2 = param2

        def notify(self, message):
            self.messages.append({'param1': self.param1, 'param2': self.param2, 'message': message})

    @request.addfinalizer
    def cleanup(): # pylint: disable=unused-variable
        woof.backends.base.BACKENDS.remove(CustomBackend)

    return CustomBackend

@pytest.fixture
def environ_set(request):

    def set(key, value):
        prev = os.environ.get(key)
        os.environ[key] = value
        @request.addfinalizer
        def cleanup(): # pylint: disable=unused-variable
            if prev is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = prev
    return set
