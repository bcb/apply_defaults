from unittest.mock import sentinel
from configparser import ConfigParser

from apply_defaults.decorators import apply_self, apply_config


config = ConfigParser()


class DummyObject:
    def __init__(self):
        self.foo = sentinel.foo

    @apply_self
    def method_with_self_applied(self, foo=None):
        return foo

    @apply_config(config)
    def method_with_config_applied(self, foo=None):
        return foo


@apply_config(config)
def function_with_config_applied(foo=None):
    return foo


@apply_config(config)
def function_with_int_applied(foo: int = None):
    return foo


@apply_config(config)
def function_with_float_applied(foo: float = 0.0):
    return foo


@apply_config(config)
def function_with_bool_applied(foo: bool = False):
    return foo


class TestApplySelf:
    def test(self):
        assert DummyObject().method_with_self_applied() is sentinel.foo

    def test_override(self):
        assert DummyObject().method_with_self_applied(foo=sentinel.foo) is sentinel.foo


class TestApplyConfig:
    def setup_module(self):
        config.remove_section("general")

    def test_with_no_config(self):
        assert DummyObject().method_with_config_applied() is None

    def test_with_config(self):
        config.read_dict({"general": {"foo": sentinel.foo}})
        assert DummyObject().method_with_config_applied() == "sentinel.foo"

    def test_override(self):
        config.read_dict({"general": {"foo": sentinel.foo}})
        assert DummyObject().method_with_config_applied(foo="bar") is "bar"

    def test_apply_to_function(self):
        config.read_dict({"general": {"foo": sentinel.foo}})
        assert function_with_config_applied(foo="bar") is "bar"

    def test_int(self):
        config.read_dict({"general": {"foo": "1"}})
        result = function_with_int_applied()
        assert result == 1
        assert type(result) is int

    def test_float(self):
        config.read_dict({"general": {"foo": "1.1"}})
        result = function_with_float_applied()
        assert result == 1.1
        assert type(result) is float

    def test_bool(self):
        config.read_dict({"general": {"foo": "True"}})
        result = function_with_bool_applied()
        assert result == True
        assert type(result) is bool
