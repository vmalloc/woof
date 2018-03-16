import woof


def test_woof_not_configured(custom_backend_class):
    woof.notify('hey')
    assert custom_backend_class.messages == []


def test_woof_configured(custom_backend_class, environ_set):
    environ_set('WOOF_CUSTOM_PARAM1', 'param1_value')
    environ_set('WOOF_CUSTOM_PARAM2', 'param2_value')
    woof.notify('hey')
    assert custom_backend_class.messages == [{
        'param1': 'param1_value',
        'param2': 'param2_value',
        'message': 'hey',

    }]
