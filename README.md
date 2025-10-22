# xarray integration for marray

[![docs](https://readthedocs.org/projects/marray-xarray/badge/?version=latest)](https://marray-xarray.readthedocs.io)
[![codestyle](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

> [!NOTE]
> This package is experimental and will need quite a bit of work to be usable.

[marray](https://github.com/mdhaber/marray) provides a array API-compliant masked array implementation.

This resolves `xarray`'s long-standing issue of not supporting missing values in arrays of non-floating point / complex dtypes — in particular `int` and `bool` — and conflating the concepts of missing values and the result of invalid operations (floating point `NaN`).

`marray-xarray` provides convenience methods for using `marray` with `xarray`, such as converting arrays to masked arrays, modifying their mask, or filling the masked values.

```python
import marray_xarray  # noqa: F401
import xarray as xr

ds = xr.tutorial.open_dataset("air_temperature").load()
ds.masked.where(ds["lon"] > 40)
```
