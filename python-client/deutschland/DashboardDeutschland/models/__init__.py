# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from deutschland.DashboardDeutschland.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from deutschland.DashboardDeutschland.model.geo import Geo
from deutschland.DashboardDeutschland.model.geo_crs import GeoCrs
from deutschland.DashboardDeutschland.model.geo_crs_properties import GeoCrsProperties
from deutschland.DashboardDeutschland.model.get import Get
from deutschland.DashboardDeutschland.model.get_category import GetCategory
from deutschland.DashboardDeutschland.model.get_layout_tiles import GetLayoutTiles
from deutschland.DashboardDeutschland.model.indicators import Indicators
