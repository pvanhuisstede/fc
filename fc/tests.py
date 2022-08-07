# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_tests.ipynb.

# %% auto 0
__all__ = []

# %% ../00_tests.ipynb 3
from fastai import *
from fastcore import *
from fastcore.foundation import *
from fastcore.utils import *
from fastcore.test import *
from nbdev.showdoc import *
from fastcore.nb_imports import *

# %% ../00_tests.ipynb 6
show_doc(test_fail)

# %% ../00_tests.ipynb 7
def _fail(): raise Exception("foobar")
test_fail(_fail, contains="bar")

def _fail(): raise Exception()
test_fail(_fail)

# %% ../00_tests.ipynb 9
def _fail_args(a):
    if a == 5:
        raise ValueError
test_fail(_fail_args, args=(5,))
test_fail(_fail_args, kwargs=dict(a=5))

# %% ../00_tests.ipynb 11
show_doc(test)