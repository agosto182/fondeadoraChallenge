import unittest
from main import plain_deep_int_array

class TestUtils(unittest.TestCase):
  def test_should_raise_exception_on_invalid_input(self):
    array_to_test = [1, [2, [3, [4, "not number"]]]]
  
    with self.assertRaises(Exception):
      plain_deep_int_array(array_to_test)

  def test_challenge_example_array_test(self):
    array_to_test = [1, [2, [3, [4, 5]]]]
    res = plain_deep_int_array(array_to_test)
  
    self.assertEqual(res, [1, 2, 3, 4, 5])

  def test_function_plain_deep_int_array_should_plain_hard_list(self):
    array_to_test = [1,[2,3], [4, [5,6,[7]]], 8, 9, [[10]]]
    res = plain_deep_int_array(array_to_test)
  
    for x in range(10):
      self.assertEqual(res[x], x+1)

if __name__ == '__main__':
    unittest.main()