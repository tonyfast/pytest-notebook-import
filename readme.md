
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/tonyfast/pytest-notebook-import/master?urlpath=lab/tree/readme.ipynb)

Import pytest plugins for hypothesis, coverage, and benchmarking.


```python
from IPython import get_ipython
```


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
from importnb import Notebook
with Notebook():  
    from fixtures import *
```

    Overwriting conftest.py



```python
%%file test_py.py
def test_py(): assert True
```

    Overwriting test_py.py



```python
def test_something_in_readme():
    assert True
```

Use the pytest api.


```python
if __name__ == '__main__':
    __import__('pytest').main(args=[])    
```

    =============================== test session starts ===============================
    platform darwin -- Python 3.6.3, pytest-3.5.1, py-1.5.3, pluggy-0.6.0
    benchmark: 3.1.1 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
    rootdir: /Users/tonyfast/_test, inifile:
    plugins: cov-2.5.1, benchmark-3.1.1, hypothesis-3.56.5, importnb-0.2.1
    collected 6 items
    
    readme.ipynb .                                                              [ 16%]
    test_notebook.ipynb ...                                                     [ 66%]
    test_py.py ..
    
    
    ----------------------------------------------- benchmark: 1 tests -----------------------------------------------
    Name (time in ms)          Min       Max      Mean  StdDev    Median     IQR  Outliers     OPS  Rounds  Iterations
    ------------------------------------------------------------------------------------------------------------------
    test_sleep            200.5244  204.5069  202.2543  1.5362  201.9491  2.1844       2;0  4.9443       5           1
    ------------------------------------------------------------------------------------------------------------------
    
    Legend:
      Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
      OPS: Operations Per Second, computed as 1 / Mean
    ============================ 6 passed in 2.80 seconds =============================


User ipython to test files with magics.


```python
if __name__ == '__main__':
    !source activate p6 && ipython -m pytest
```

    ]0;IPython: tonyfast/_test[1m============================= test session starts ==============================[0m
    platform darwin -- Python 3.6.3, pytest-3.5.1, py-1.5.3, pluggy-0.6.0
    benchmark: 3.1.1 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
    rootdir: /Users/tonyfast/_test, inifile:
    plugins: cov-2.5.1, benchmark-3.1.1, hypothesis-3.56.5, importnb-0.2.1
    collected 1 item                                                               [0m
    
    readme.ipynb .[36m                                                           [100%][0m
    
    [32m[1m=========================== 1 passed in 0.01 seconds ===========================[0m


Make the readme.


```python
if __name__ == '__main__':
    !jupyter nbconvert --to markdown readme.ipynb
```

    [NbConvertApp] Converting notebook readme.ipynb to markdown
    [NbConvertApp] Writing 10154 bytes to readme.md

