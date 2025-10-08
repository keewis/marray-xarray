from importlib.metadata import version

from marray_xarray.accessors import (  # noqa: F401
    MarrayDataArrayAccessor,
    MarrayDatasetAccessor,
)

try:
    __version__ = version("marray_xarray")
except Exception:
    __version__ = "9999"
