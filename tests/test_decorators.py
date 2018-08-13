from apply_defaults.decorators import apply_self, apply_config
from unittest.mock import sentinel
from configparser import ConfigParser


config = ConfigParser()
config.read_dict({"general": {"foo": "foo"}})


class Dummy:
    def __init__(self):
        self.foo = sentinel

    @apply_self
    def apply_self(self, foo=None):
        return foo

    @apply_config(config)
    def apply_config(self, foo=None):
        return foo


@apply_config(config)
def dummy_func(foo=None):
    return foo



def test_apply_self():
    assert Dummy().apply_self() is sentinel


def test_apply_self_override():
    assert Dummy().apply_self(foo="foo") is "foo"


def test_apply_config():
    assert Dummy().apply_config() is "foo"


def test_apply_config_override():
    assert Dummy().apply_config(foo="bar") is "bar"


def test_apply_config_to_function():
    assert dummy_func(foo="bar") is "bar"
