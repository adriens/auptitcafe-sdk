# Changelog

All notable changes to this project will be documented in this file.

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
