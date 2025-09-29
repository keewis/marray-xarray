from importlib.metadata import version

from marray_xarray.accessors import MarrayAccessor  # noqa: F401

try:
    __version__ = version("marray_xarray")
except Exception:
    __version__ = "9999"
