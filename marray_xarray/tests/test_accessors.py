import marray
import numpy as np
import pytest
import xarray as xr

from marray_xarray import accessors  # noqa: F401

mnp = marray.masked_namespace(np)


class TestDataArrayAccessor:
    @pytest.mark.parametrize(
        ["array", "mask", "expected"],
        (
            (
                xr.DataArray(np.arange(3), dims="x"),
                xr.DataArray([True, False, True], dims="x"),
                xr.DataArray(
                    mnp.asarray(np.arange(3), mask=[True, False, True]), dims="x"
                ),
            ),
            (
                xr.DataArray(np.arange(6).reshape(2, 3), dims=["x", "y"]),
                xr.DataArray([True, False], dims="x"),
                xr.DataArray(
                    mnp.asarray(
                        np.arange(6).reshape(2, 3),
                        mask=np.array([[True, True, True], [False, False, False]]),
                    ),
                    dims=["x", "y"],
                ),
            ),
        ),
    )
    def test_where(self, array, mask, expected):
        actual = array.masked.where(mask)

        xr.testing.assert_equal(actual, expected)
