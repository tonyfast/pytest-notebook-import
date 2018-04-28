
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

import pytest
from importnb import Notebook

with Notebook():  
    from fixtures import *

def pytest_collect_file(parent, path):
    if path.ext in (".ipynb", ".py"):
        return Module(path, parent)
    
class Module(pytest.Module):
    def collect(self):
        with Notebook(): 
            return super().collect()
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
    plugins: cov-2.5.1, benchmark-3.1.1, hypothesis-3.56.5
    collected 4 items / 1 errors
    
    ================================== ERRORS ==================================
    _________________________ ERROR collecting test.py _________________________
    ImportError while importing test module '/Users/tonyfast/_test/test.py'.
    Hint: make sure your test modules/packages have valid Python names.
    Traceback:
    test.py:2: in <module>
        from a_test_notebook import *
    E   ModuleNotFoundError: No module named 'a_test_notebook'
    ============================= warnings summary =============================
    None
      Module already imported so cannot be rewritten: pytest_cov
      Module already imported so cannot be rewritten: pytest_benchmark
      Module already imported so cannot be rewritten: hypothesis
    
    -- Docs: http://doc.pytest.org/en/latest/warnings.html
    !!!!!!!!!!!!!!!!! Interrupted: 1 errors during collection !!!!!!!!!!!!!!!!!!
    =================== 3 warnings, 1 error in 0.11 seconds ====================
    [NbConvertApp] Converting notebook readme.ipynb to markdown
    [NbConvertApp] Writing 2603 bytes to readme.md

