from types import ModuleType

import hypothesis.strategies as st
import marray
import numpy as np
from xarray_array_testing.base import DuckArrayTestMixin
from xarray_array_testing.creation import CreationTests
from xarray_array_testing.indexing import IndexingTests
from xarray_array_testing.reduction import ReductionTests

mxp = marray.masked_namespace(np)


def create_masked_array(*, shape, dtype):
    return st.builds(mxp.ones, shape=st.just(shape), dtype=st.just(dtype))


class MArrayTestMixin(DuckArrayTestMixin):
    @property
    def xp(self) -> ModuleType:
        return mxp

    @property
    def array_type(self) -> type[mxp.MArray]:
        return mxp.MArray

    @staticmethod
    def array_strategy_fn(*, shape, dtype):
        return create_masked_array(shape=shape, dtype=dtype)


class TestCreationMArray(CreationTests, MArrayTestMixin):
    pass


class TestReductionMArray(ReductionTests, MArrayTestMixin):
    pass


class TestIndexingMArray(IndexingTests, MArrayTestMixin):
    pass
