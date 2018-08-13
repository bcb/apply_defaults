# apply_defaults

Applies a set of values to a function's optional params, if nothing was passed
to them. The values can come from the bound object, or a configuration file.

`apply_self` applies attributes from the bound object:

```python
from apply_defaults import apply_self

class MyObject:
    def __init__(self):
        self.foo = "foo"

    @apply_self
    def method(self, foo=None):
        return foo

>>> # If 'foo' is not passed, the param is assigned the value of self.foo.
>>> MyObject().method()
'foo'
>>> # Overriding @apply_self by specifying a value for 'foo'.
>>> MyObject().method(foo="bar")
'bar'
```

`apply_config` applies the options from a ConfigParser:

```python
from apply_defaults import apply_config
from configparser import ConfigParser

config = ConfigParser()

@apply_config(config)
def my_func(foo=None)
    return foo

>>> # There is no configuration yet, so my_func returns the optional
>>> # parameter's default value.
>>> my_func()
None
>>> config.read_dict({"general": {"foo": "foo"}})
>>> # If 'foo' is not passed, the param is assigned the value of 'foo' in the
>>> # configuration.
>>> my_func()
'foo'
>>> # Override @apply_config by specifying a value for 'foo'.
>>> my_func(foo="bar")
'bar'
```
