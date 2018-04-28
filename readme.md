
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/tonyfast/pytest-notebook-import/master?urlpath=lab/tree/readme.ipynb)

Import the notebooks you desire to test in `test_.py`.


```python
%%file test_.py
__import__('importnb').load_ipython_extension()
from a_test_notebook import *
```

    Overwriting test_.py


> `test_.py` is the most minimal name to trigger tests.

Import pytest plugins for hypothesis, coverage, and benchmarking.


```python
%%file requirements.txt
importnb
pytest
hypothesis
pytest-cov
pytest-benchmark
```

    Overwriting requirements.txt


We can even create test fixtures in a notebook and load them into `conftest.py`


```python
%%file conftest.py
__import__('importnb').load_ipython_extension()
from fixtures import *
```

    Overwriting conftest.py



```python
if __name__ == '__main__':
    __import__('pytest').main(args=[])
    !jupyter nbconvert --to markdown readme.ipynb
```

    =========================== test session starts ============================
    platform darwin -- Python 3.6.3, pytest-3.5.1, py-1.5.3, pluggy-0.6.0
    benchmark: 3.1.1 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
    rootdir: /Users/tonyfast/_test, inifile:
    plugins: cov-2.5.1, benchmark-3.1.1, hypothesis-3.56.5
    collected 3 items
    
    test_.py ...                                                         [100%]
    
    
    ----------------------------------------------- benchmark: 1 tests -----------------------------------------------
    Name (time in ms)          Min       Max      Mean  StdDev    Median     IQR  Outliers     OPS  Rounds  Iterations
    ------------------------------------------------------------------------------------------------------------------
    test_sleep            200.5592  205.1243  202.7852  2.0669  202.4509  3.8508       2;0  4.9313       5           1
    ------------------------------------------------------------------------------------------------------------------
    
    Legend:
      Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
      OPS: Operations Per Second, computed as 1 / Mean
    ========================= 3 passed in 2.79 seconds =========================
    [NbConvertApp] Converting notebook readme.ipynb to markdown
    [NbConvertApp] Writing 2829 bytes to readme.md

