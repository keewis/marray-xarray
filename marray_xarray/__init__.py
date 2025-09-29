from importlib.metadata import version

try:
    __version__ = version("marray_xarray")
except Exception:
    __version__ = "9999"
