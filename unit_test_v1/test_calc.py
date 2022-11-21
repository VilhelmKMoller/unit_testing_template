import unittest
## The module i want to test
import calc

## UNITTEST documentation: https://docs.python.org/3/library/unittest.html


## create test cases in test class

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        # result = calc.add(10, 5) 
        # self.assertEqual(result, 15)

        ## Remember to test edge cases
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
    
    def test_subtract(self):
        ## Remember to test edge cases
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        ## Remember to test edge cases
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
    
    def test_divide(self):
        ## Remember to test edge cases
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # (exeption, function, argument 1, argument 2)
        # self.assertRaises(ValueError, calc.divide, 10, 0)

        # test exeption using context manager:
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


# Run directly in python and it will run the test. But only if you run it directly.
if __name__ == '__main__':
    unittest.main()
