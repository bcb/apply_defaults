from apply_defaults.decorators import apply_self, apply_config
from unittest.mock import sentinel
from configparser import ConfigParser


class ApplySelf:
    def __init__(self):
        self.foo = sentinel

    @apply_self
    def meth(self, foo=None):
        return foo


config = ConfigParser()
config.read_dict({'general': {'foo': 'foo'}})

class ApplyConfig:
    def __init__(self):
        self.foo = sentinel

    @apply_config(config)
    def meth(self, foo=None):
        return foo


def test_apply_self():
    assert ApplySelf().meth() is sentinel

def test_apply_self_override():
    assert ApplySelf().meth(foo="foo") is "foo"

def test_apply_config():
    assert ApplyConfig().meth() is 'foo'

def test_apply_config_override():
    assert ApplyConfig().meth(foo="bar") is 'bar'
