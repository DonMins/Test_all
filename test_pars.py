import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import src.pars

class TestUM:

 def test_num (self):
  assert src.pars.parse('1.1') == 1.1

 def test_neg(self):
  assert src.pars.parse('-2') == -2

 def test_complex_num_sub(self):
  assert  src.pars.parse('2 - 1j') == ['apply', '-', [2.0, 1j]]

 def test_func_calc_args(self):
  assert  src.pars.parse('sin(2)') ==['apply', 'sin', [2.0]]

 def test_assign_add_pow(self):
   assert   src.pars.parse('z = x + y^3') == ['set', 'z', ['apply', '+', ['x', ['apply', 'pow', ['y', 3.0]]]]]

 def test_unset(self):
    assert   src.pars.parse('unset x')==['unset', 'x']

 def test_mul_var_args_def_func(self):
    assert  src.pars.parse('def f(x, y) = (2 + x) * y')==['def', 'f', ['x', 'y'], ['apply', '*', [['apply', '+', [2.0, 'x']], 'y']]]

 def test_undef(self):
    assert  src.pars.parse('undef f')==['undef', 'f']

 def test_matrix(self):
    assert  src.pars.parse('[[1 2] [3 4]]')==['matrix', [['matrix', [1.0, 2.0]], ['matrix', [3.0, 4.0]]]]

 def test_div(self):
  assert  src.pars.parse('(1 + 2) / 3')==['apply', '/', [['apply', '+', [1.0, 2.0]], 3.0]]

 def test_unit_div(self):
  assert src.pars. parse('2 {kg/c}')==['with_units', 2.0, ['unit_div', ['unit', 'kg'], 'c']]

 def test_unit_mul(self):
    assert  src.pars.parse('2 {kg*c}') ==['with_units', 2.0, ['unit_mul', ['unit', 'kg'], 'c']]
