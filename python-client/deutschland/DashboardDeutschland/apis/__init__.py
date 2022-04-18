# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from deutschland.DashboardDeutschland.api.geo_api import GeoApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from deutschland.DashboardDeutschland.api.geo_api import GeoApi
from deutschland.DashboardDeutschland.api.get_api import GetApi
from deutschland.DashboardDeutschland.api.indicators_api import IndicatorsApi
