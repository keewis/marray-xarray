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
        """
        return self.obj.map(partial(mask_array, condition=condition))
