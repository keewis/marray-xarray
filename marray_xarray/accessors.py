from functools import partial

import xarray as xr

from marray_xarray.masking import mask_array


@xr.register_dataset_accessor("masked")
@xr.register_dataarray_accessor("masked")
class MarrayAccessor:
    def __init__(self, obj):
        self._obj = obj

    def where(self, condition):
        if isinstance(self._obj, xr.Dataset):
            return self._obj.map(partial(mask_array, condition=condition))
        else:
            return mask_array(self._obj, condition)
