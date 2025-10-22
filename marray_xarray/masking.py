import marray


def mask_array(arr, condition):
    xp = arr.data.__array_namespace__()
    mxp = marray.masked_namespace(xp)

    NA = mxp.asarray(0, mask=True)

    return arr.where(condition, NA)
