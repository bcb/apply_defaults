# apply_defaults

Applies a set of values to a function's optional parameters, if nothing was
passed to them.

In Python, a function receives:
1. the passed value, if specified, otherwise
2. the default value in the parameter list.

These decorators add another layer in between, so it receives:

1. the passed value, if specified, otherwise
2. *the value from another set*, if specified, otherwise
3. the default value in the parameter list.

The values can come from the bound object or a configuration object.

## apply_self

This decorator applies values from the bound object:

```python
from apply_defaults import apply_self

class MyObject:
    def __init__(self):
        self.foo = "foo"

    @apply_self
    def method(self, foo=None):
        return foo

>>> # A value is passed - this takes precedence.
>>> MyObject().method(foo="bar")
'bar'
>>> # A value is not passed, so self.foo is used.
>>> MyObject().method()
'foo'
```

## apply_config

This decorator applies the options from a ConfigParser object:

```python
from apply_defaults import apply_config
from configparser import ConfigParser

config = ConfigParser()

@apply_config(config)
def my_func(foo=None)
    return foo

>>> # A value is passed - this takes precedence.
>>> my_func(foo="bar")
'bar'
>>> # There is no configuration yet; so my_func takes the parameter's
>>> # default value.
>>> my_func()
None
>>> # Let's load some configuration. Now when foo is not passed, the param
>>> # takes the value from the configuration.
>>> config.read_dict({"general": {"foo": "foo"}})
>>> my_func()
'foo'
```
