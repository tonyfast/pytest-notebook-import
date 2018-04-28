
import pytest
from importnb import Notebook

with Notebook(): from fixtures import *

def pytest_collect_file(parent, path):
    if path.ext in (".ipynb", ".py"): return Module(path, parent)
    
class Module(pytest.Module):
    def collect(self):
        with Notebook(): return super().collect()