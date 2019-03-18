import pytest

from pandarallel import pandarallel

import pandas as _pd
import numpy as np
import math


def test_docs() :

    # create dummy df
    df = _pd.DataFrame({"d" : np.random.randint(0, 1000, 1000)})
    pandarallel.initialize()

    # validate df.apply == df.parallel_apply
    def f(i) :
        return i**2

    df_apply    = df.apply(f, axis=1)
    df_parallel = df.parallel_apply(f, axis=1)
    assert (df_apply.d == df_parallel.d).all()

    # doc
    assert df.apply.__doc__ == df.parallel_apply.__doc__


