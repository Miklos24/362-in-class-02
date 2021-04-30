import calculator
import unittest

class TestCase(unittest.TestCase):
    def test_add_basic(self):
        self.assertEqual(5, calculator.add(2, 3))
    
    def test_add_val_error(self):
        self.assertRaises(ValueError, calculator.add("fish", 3))
    
    def test_subtract_basic(self):
        self.assertEqual(1, calculator.subtract(3, 2))

    def test_subtract_neg(self):
        self.assertEqual(-1, calculator.subtract(2, 3))
    
    def test_multiply_basic(self):
        self.assertEqual(6, calculator.multiply(2, 3))

    def test_multiply_list(self):
        self.assertEqual([4, 6], calculator.multiply(2, [2, 3]))
    
    def test_divide_basic(self):
        self.assertEqual(2, calculator.divide(8, 4))
    
    def test_divide_float(self):
        self.assertEqual(2.5, calculator.divide(5, 2))
    


if __name__ == '__main__':
    unittest.main()