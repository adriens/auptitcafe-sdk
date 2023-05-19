![PyPI - Implementation](https://img.shields.io/pypi/implementation/auptitcafe)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/auptitcafe)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/auptitcafe)
![PyPI - Format](https://img.shields.io/pypi/format/auptitcafe)
![PyPI](https://img.shields.io/pypi/v/auptitcafe)

# 🔖 Resources

- http://auptitcafe.nc/
- [Au P'tit Cafe on TripAdvisor](https://www.tripadvisor.com/Restaurant_Review-g294130-d1952994-Reviews-Au_P_tit_Cafe-Noumea_Grand_Terre.html)
- [`auptitcafe`](https://pypi.org/project/auptitcafe/) on `pypi`
- [`auptitcafe`](https://www.instagram.com/auptitcafe.nc/?hl=en) sur Instagram
- [`auptitcafe`](https://www.facebook.com/auptitcafe.nc/) sur Facebook

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/iRSInif_Zwc/0.jpg)](https://www.youtube.com/watch?v=iRSInif_Zwc)


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
