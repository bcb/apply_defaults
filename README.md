# apply_defaults

Apply default values to functions.

Makes configuration easy! Application settings come from a config file into
your code cleanly and with minimal effort.

No more `val = val if val is not None else config.val if 'val' in config else
val` ugliness.

```sh
pip install apply_defaults
```

## apply_config

This decorator applies options from a ConfigParser object.

```python
from apply_defaults import apply_config
from configparser import ConfigParser

config = ConfigParser()
config.read_dict({"general": {"option": True}})  # alteratively read a file

@apply_config(config)
def func(option: bool = False) -> bool:
    return option
```

The `option` parameter takes the value from the configuration.

```python
>>> func()
True
```

Override the configuration by passing a value.

```python
>>> func(option=False)
'False'
```

If the option is not in the configuration, the default value from the parameter
list is used.

```python
>>> config.remove_option("general", "option")
>>> func()
False
```

_Note: ConfigParser's options are strings. Type hints in the function signature
allow the apply_config decorator to cast options to the desired type.
Alternatively cast the value yourself._

## apply_self

This decorator applies attributes from the bound object.

```python
from apply_defaults import apply_self

class MyObject:
    def __init__(self):
        self.option = True

    @apply_self
    def func(self, option=False):
        return value
```

_Type hints allow the decorator to cast the config option to the desired type.
Otherwise, the config option will be a string every time._

The parameter takes the value from the bound object, i.e. `self.foo`.

```python
>>> obj = MyObject()
>>> obj.func()
True
```

Override by passing a value.

```python
>>> obj.func(option=False)
False
```

If the attribute is not in the bound object, the default value from the
parameter list is used.

```python
>>> del obj.option
>>> obj.func()
False
```
