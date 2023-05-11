![PyPI - Implementation](https://img.shields.io/pypi/implementation/auptitcafe)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/auptitcafe)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/auptitcafe)
![PyPI - Format](https://img.shields.io/pypi/format/auptitcafe)
![PyPI](https://img.shields.io/pypi/v/auptitcafe)

# Quickstart

```python
!pip install auptitcafe

from auptitcafe.menus import Menus

menu_instance = Menus()
menus = []
menus = menu_instance.get_all()
len(menus)
```

# For devs

## Build

```
poetry show --tree
```

```
poetry build
poetry install
```

## test

```
poetry run pytest
```



## Publish

```
poetry config pypi-token.pypi $PYPI_TOKEM
poetry publish
```
