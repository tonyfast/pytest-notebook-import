
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/tonyfast/pytest-notebook-import/master?urlpath=lab/tree/readme.ipynb)

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
%%file test_py.py
def test_py(): assert True
```

    Overwriting test_py.py



```python
%%file pytest.ini
[pytest]
python_files=test_*.['ipynb', 'py']
```

    Overwriting pytest.ini



```python
%%file conftest.py
from importnb import Notebook
with Notebook():  
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
    rootdir: /Users/tonyfast/_test, inifile: pytest.ini
    plugins: cov-2.5.1, benchmark-3.1.1, hypothesis-3.56.5, importnb-0.2.1
    collected 4 items
    
    test_notebook.ipynb ...                                              [ 75%]
    test_py.py .                                                         [100%]
    
    
    ----------------------------------------------- benchmark: 1 tests -----------------------------------------------
    Name (time in ms)          Min       Max      Mean  StdDev    Median     IQR  Outliers     OPS  Rounds  Iterations
    ------------------------------------------------------------------------------------------------------------------
    test_sleep            201.1883  205.1336  203.5392  1.6747  203.5252  2.7777       1;0  4.9131       5           1
    ------------------------------------------------------------------------------------------------------------------
    
    Legend:
      Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
      OPS: Operations Per Second, computed as 1 / Mean
    ========================= 4 passed in 2.81 seconds =========================
    [NbConvertApp] Converting notebook readme.ipynb to markdown
    [NbConvertApp] Writing 3271 bytes to readme.md

