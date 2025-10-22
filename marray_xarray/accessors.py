from dataclasses import dataclass
from functools import partial

import xarray as xr

from marray_xarray.masking import mask_array


@xr.register_dataarray_accessor("masked")
@dataclass
class MarrayDataArrayAccessor:
    obj: xr.DataArray

    def where(self, condition):
        """Mask by condition

        If already masked, the new mask will be combined with the existing mask using
        logical or.

        Parameters
        ----------
        condition : xr.DataArray
            New mask for the array.

        Returns
        -------
        masked : xr.DataArray
            The input array's data converted to a ``marray`` object or with an
            updated mask.

        Notes
        -----
        If the array namespace is known, this operation can also be done using
        :py:meth:`xarray.DataArray.where` and the constant
        ``mxp.asarray(0, mask=True)``.

        Examples
        --------
        >>> data = np.arange(10)
        >>> arr = xr.DataArray(data, dims="x")
        >>> arr
        <xarray.DataArray (x: 10)> Size: 80B
        array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        Dimensions without coordinates: x
        >>> mask = data % 2 == 1
        >>> masked = arr.masked.where(mask)
        >>> masked
        <xarray.DataArray (x: 10)> Size: 80B
        MArray(
            array([ _, 1, _, 3, _, 5, _, 7, _, 9]),
            array([ True, False,  True, False,  True, False,  True, False,  True,
                   False])
        )
        Dimensions without coordinates: x
        """
        return mask_array(self.obj, condition=condition)


@xr.register_dataset_accessor("masked")
@dataclass
class MarrayDatasetAccessor:
    obj: xr.Dataset

    def where(self, condition):
        """Mask by condition

        If already masked, the new mask will be combined with the existing mask using
        logical or.

        Parameters
        ----------
        condition : xr.DataArray
            New mask for the array.

        Returns
        -------
        masked : xr.Dataset
            The data of the data variables converted to ``marray`` objects or with
            updated masks.

        Notes
        -----
        If the array namespace is known and the same for all data variables,
        this operation can also be done using :py:meth:`xarray.Dataset.where`
        and the constant ``mxp.asarray(0, mask=True)``.

        Examples
        --------
        >>> data1 = np.arange(10)
        >>> data2 = np.linspace(0, 1, 10, dtype="float64")
        >>> ds = xr.Dataset({"a": ("x", data1), "b": ("x", data2)})
        >>> ds
        <xarray.Dataset> Size: 160B
        Dimensions:  (x: 10)
        Dimensions without coordinates: x
        Data variables:
            a        (x) int64 80B 0 1 2 3 4 5 6 7 8 9
            b        (x) float64 80B 0.0 0.1111 0.2222 0.3333 ... 0.7778 0.8889 1.0
        >>> mask = data1 % 2 == 1
        >>> masked = ds.masked.where(mask)
        >>> masked
        <xarray.Dataset> Size: 160B
        Dimensions:  (x: 10)
        Dimensions without coordinates: x
        Data variables:
            a        (x) int64 80B ...
            b        (x) float64 80B ...
        """
        return self.obj.map(partial(mask_array, condition=condition))
