from apply_defaults.decorators import apply_self, apply_config
from unittest.mock import sentinel
from configparser import ConfigParser


class ApplySelf:
    def __init__(self):
        self.foo = sentinel

    @apply_self
    def meth(self, foo=None):
        return foo


class ApplyConfig:
    def __init__(self):
        self.foo = sentinel

    @apply_config(ConfigParser())
    def meth(self, foo=None):
        return foo


def test_apply_self():
    assert ApplySelf().meth() is sentinel

def test_apply_self_override():
    assert ApplySelf().meth(foo="foo") == "foo"

def test_apply_config():
    assert ApplyConfig().meth() is sentinel
