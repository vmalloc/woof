import os
import inspect

BACKENDS = []


class _BackendMeta(type):

    def __new__(*args, **kwargs):
        cls = type.__new__(*args, **kwargs)
        BACKENDS.append(cls)
        return cls


class Backend(metaclass=_BackendMeta):

    @property
    def name(self):
        returned = type(self).__name__
        assert returned.endswith('Backend')
        return returned.split('Backend')[0]

    @classmethod
    def try_configure(cls):
        arg_names = inspect.getargspec(cls.__init__).args[1:]
        backend_name = cls.__name__.lower().split('backend')[0]

        kwargs = {}
        for arg_name in arg_names:
            arg_value = os.environ.get(f'WOOF_{backend_name.upper()}_{arg_name.upper()}')
            if arg_value is None:
                return None
            kwargs[arg_name] = arg_value
        return cls(**kwargs)

BACKENDS.remove(Backend)
