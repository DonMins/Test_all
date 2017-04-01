
import math
import pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import src.calc

class TestUM:

 def test_sum(self):
    assert src.calc.calculate('e', src.calc.Environment()) == math.e

 def test_su(self):
     assert src.calc.calculate('cos(0)', src.calc.Environment()) == 1.0

 def test_su1(self):
        assert src.calc.calculate('tr(T([2 1]) * [1 2])', src.calc.Environment()) == 4

 def test_set_func_(self):
     env = src.calc.Environment()
     src.calc.calculate('def f(x,y) = x + y', env)
     env.get_function('f')

 def test_set_var_(self):
     env = src.calc.Environment()
     src.calc.calculate('x = 1', env)
     env.get_var('x')

 def test_get_var_(self):
     env = src.calc.Environment()
     with pytest.raises(RuntimeError):
      env.get_var('x')

 def test_get_va(self):
     env = src.calc.Environment()
     with pytest.raises(RuntimeError):
      env.get_var('x')

 def test_del_var_(self):
     env = src.calc.Environment()
     src.calc.calculate('x = 1', env)
     env.del_var('x')

 def test_del_var1(self):
     env = src.calc.Environment()
     env.del_var('x')

 def test_undef_func(self):
     env = src.calc.Environment()
     with pytest.raises(RuntimeError):
          env.get_function('f')

