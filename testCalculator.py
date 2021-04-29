import calculator
import unittest

class TestCase(unittest.TestCase):
    def test_add_basic(self):
        self.assertEqual(5, calculator.add(2, 3))
    
    def test_add_error(self):
        self.assertRaises(ValueError, calculator.add("fish", 3))
    
    def test_subtract(self):
        self.assertEqual(-1, calculator.subtract(2, 3))
    
    def test_multiply(self):
        self.assertEqual(6, calculator.multiply(2, 3))
    
    def test_divide_int(self):
        self.assertEqual(2, calculator.divide(8, 4))
    
    def test_divide_float(self):
        self.assertEqual(2.5, calculator.divide(5, 2))
    


if __name__ == '__main__':
    unittest.main()