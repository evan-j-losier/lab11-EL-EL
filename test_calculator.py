# https://github.com/evan-j-losier/lab11-EL-EL.git
# Partner 1: Evan Losier
# Partner 2: Enric Lin

import unittest
import calculator

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(10, 5), 15)
        self.assertEqual(calculator.add(-2, 2), 0)

    def test_subtract(self):
        self.assertEqual(calculator.sub(2, 3), -1)
        self.assertEqual(calculator.sub(10, 5), 5)
        self.assertEqual(calculator.sub(-2, 2), -4)
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    def test_multiply(self): # 3 assertions
        self.assertEqual(calculator.mul(2, 3), 6)
        self.assertEqual(calculator.mul(10, 5), 50)
        self.assertEqual(calculator.mul(-2, 2), -4)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(calculator.div(2, 4), 1/2)
        self.assertEqual(calculator.div(10, 5), 2)
        self.assertEqual(calculator.div(-2, 2), -1)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.log(2, 8), 3)
        self.assertAlmostEqual(calculator.log(10, 100), 2)
        self.assertAlmostEqual(calculator.log(3, 27), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.log(1, 8)
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(calculator.hypotenuse(3, 4), 5)
        self.assertEqual(calculator.hypotenuse(-5, 12), 13)
        self.assertEqual(calculator.hypotenuse(8, -15), 17)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(calculator.square_root(9),3)
        self.assertEqual(calculator.square_root(16),4)
        self.assertEqual(calculator.square_root(64),8)


# Do not touch this
if __name__ == "__main__":
    unittest.main()