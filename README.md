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
