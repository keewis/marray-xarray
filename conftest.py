import pytest


@pytest.fixture(autouse=True)
def doctest_setup(doctest_namespace, tmpdir):
    import marray
    import numpy as np
    import xarray as xr

    mnp = marray.masked_namespace(np)

    # imports
    doctest_namespace["np"] = np
    doctest_namespace["xr"] = xr
    doctest_namespace["marray"] = marray
    doctest_namespace["mnp"] = mnp

    # random numbers
    rng = np.random.default_rng(seed=0)
    doctest_namespace["rng"] = rng

    # make sure any files are written to a temporary directory
    tmpdir.chdir()
