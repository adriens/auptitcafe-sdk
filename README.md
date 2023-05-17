![PyPI - Implementation](https://img.shields.io/pypi/implementation/auptitcafe)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/auptitcafe)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/auptitcafe)
![PyPI - Format](https://img.shields.io/pypi/format/auptitcafe)
![PyPI](https://img.shields.io/pypi/v/auptitcafe)

# 🚀 Quickstart

For the impatients, here is a quick and ready to use code snippet:

```python
# Install the package
!pip install auptitcafe

# Make some imports
from auptitcafe.menus import Menus
import pandas as pd

# Create the main utility instance
menu_instance = Menus()

# Dump menus as a csv file
menus = 'menus.csv'
menu_instance.to_csv(menus)

# Load menus in a panda dataframe
df = pd.read_csv(menus)
# Diplay dataframe
df
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
