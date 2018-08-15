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
```

When a value is passed; take this value.

```python
>>> MyObject().method(foo="bar")
'bar'
```

However when a value is _not_ passed, `self.foo` is used.

```python
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
```

When a value is passed, take this value.

```python
>>> my_func(foo="bar")
'bar'
```

There is no configuration yet, so my_func takes the parameter's default value.

```python
>>> my_func()
None
```

With some configuration loaded, the param takes the value from the
configuration.

```python
>>> config.read_dict({"general": {"foo": "foo"}})
>>> my_func()
'foo'
```
