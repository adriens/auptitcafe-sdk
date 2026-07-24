# Changelog

All notable changes to this project will be documented in this file.

## [0.2.1] - 2026-07-25

### Fixed
- **Critical**: Fixed scraping selectors broken by auptitcafe.nc site redesign — `Menus.get_all()` and `Emporter.get_all()` were returning empty lists
- Site now serves a single page (`/#carte`) with "sur place"/"à emporter" tabs instead of separate `/menu/` and `/a-emporter/` pages

### Changed
- Updated selectors to new markup: `div#apc-sp` / `div#apc-ae` panels, `article.dish`, `span.dish-name`, `span.dish-price-amount`, `p.dish-desc`, `img.dish-img`
- `get_title()` now reads `section#carte h2`
- `Emporter.get_all()` now populates real prices for à-emporter items (previously hardcoded to `None`/`0`), since the new design displays them

### Tested
- ✅ 9 menus successfully retrieved from website
- ✅ 15 takeaway items successfully retrieved
- ✅ CSV export working correctly
- ✅ All unit tests passing

## [0.2.0] - 2025-12-13

### Fixed
- **Critical**: Fixed ModSecurity blocking (HTTP 412) by adding User-Agent header to all HTTP requests
- **Bug**: Fixed `extract_price()` function to handle edge cases like "3 CHOCOLAT - 1200F" where dish names contain numbers
- **Bug**: Fixed `extract_name()` function using rsplit() instead of finding first digit for more robust parsing

### Changed
- Added `self.headers` with User-Agent to `Menus` class `__init__()` method
- Added `self.headers` with User-Agent to `Emporter` class `__init__()` method
- Updated all `requests.get()` calls to use `headers=self.headers` parameter
- Improved price and name extraction using regex patterns for better reliability

### Tested
- ✅ 9 menus successfully retrieved from website
- ✅ 21 takeaway items successfully retrieved
- ✅ CSV export working correctly
- ✅ All unit tests passing
- ✅ Compatible with pandas DataFrames

## [0.1.24] - Previous version
- Legacy version without ModSecurity bypass
