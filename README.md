# apply_defaults

Applies a set of default values to optional parameters.

This is useful for configuring your functions/application cleanly.

```sh
pip install apply_defaults
```

## apply_config

This decorator applies the options from a ConfigParser object:

```python
from apply_defaults import apply_config
from configparser import ConfigParser

config = ConfigParser()
config.read_dict({"general": {"foo": "bar"}})

@apply_config(config)
def my_func(foo=None)
    return foo
```

When foo is passed, take that value.

```python
>>> my_func(foo="foo")
'foo'
```

When foo is not passed, the parameter takes the value from the configuration.

```python
>>> my_func()
'bar'
```

If foo is not in the configuration, it takes the default value from the
parameter list.

## apply_self

This decorator applies values from the bound object:

```python
from apply_defaults import apply_self

class MyObject:
    def __init__(self):
        self.foo = "bar"

    @apply_self
    def method(self, foo=None):
        return foo
```

When foo is passed, take that value.

```python
>>> MyObject().method(foo="foo")
'foo'
```

When foo is *not* passed, `self.foo` is used.

```python
>>> MyObject().method()
'bar'
```

If foo is not in the bound object's attributes, it takes the default value from
the parameter list.
