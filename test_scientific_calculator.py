import unittest
from scientific_calculator import MyCalculator 
import math

class MyCalculatorTest(unittest.TestCase):
    def test_add(self):
        result = MyCalculator.add(2,3)
        self.assertEqual(result,5)

    def test_subtract(self):
        result = MyCalculator.subtract(5,2)
        self.assertEqual(result,3)

    #### sine test cases
    def test_sin_positive(self):
        result = MyCalculator.sin(90)
        self.assertAlmostEqual(result,1,places=5)
    
    def test_sin_negative(self):
        result = MyCalculator.sin(-90)
        self.assertAlmostEqual(result,-1,places=5)

    def test_sin_zero(self):
        result = MyCalculator.sin(0)
        self.assertAlmostEqual(result,0,places=5)

    def test_sin_non_numeric(self):
        with self.assertRaises(ValueError):
            MyCalculator.sin("hello")

    #### cosine test cases.
    def test_cos_positive(self):
        result = MyCalculator.cos(60)
        self.assertAlmostEqual(result,0.5,places=5)
    
    def test_cos_negative(self):
        result = MyCalculator.cos(180)
        self.assertAlmostEqual(result,-1,places=5)

    def test_cos_zero(self):
        result = MyCalculator.cos(90)
        self.assertAlmostEqual(result,0,places=5)

    def test_cos_non_numeric(self):
        with self.assertRaises(ValueError):
            MyCalculator.cos("hello")

    #### tangent test cases.
    def test_tan_positive(self):
        result = MyCalculator.tan(60)
        self.assertAlmostEqual(result,1.732,places=2)
    
    def test_tan_negative(self):
        result = MyCalculator.tan(-45)
        self.assertAlmostEqual(result,-1,places=5)

    def test_tan_zero(self):
        result = MyCalculator.tan(0)
        self.assertAlmostEqual(result,0,places=5)

    def test_tan_non_numeric(self):
        with self.assertRaises(ValueError):
            MyCalculator.tan("hello")

    def test_tan_invalid(self):
        with self.assertRaises(ValueError):
            MyCalculator.tan(90)


    #### square root test cases.
    def test_sqrt_positive(self):
        result = MyCalculator.sqrt(3)
        self.assertAlmostEqual(result,1.732,places=2)

    def test_sqrt_zero(self):
        result = MyCalculator.sqrt(0)
        self.assertAlmostEqual(result,0,places=5)

    def test_sqrt_non_numeric(self):
        with self.assertRaises(ValueError):
            MyCalculator.sqrt("hello")

    def test_sqrt_invalid(self):
        with self.assertRaises(ValueError):
            MyCalculator.sqrt(-90)


    #### logarithm root test cases.
    def test_log_positive(self):
        result = MyCalculator.log(math.e)
        self.assertAlmostEqual(result,1,places=2)

    def test_log_negative(self):
        result = MyCalculator.log(1/math.e)
        self.assertAlmostEqual(result,-1,places=2)

    def test_log_zero(self):
        result = MyCalculator.log(1)
        self.assertAlmostEqual(result,0,places=5)

    def test_log_non_numeric(self):
        with self.assertRaises(ValueError):
            MyCalculator.log("hello")

    def test_log_invalid(self):
        with self.assertRaises(ValueError):
            MyCalculator.log(0)


    #### exponent root test cases.
    def test_exp_positive(self):
        result = MyCalculator.exp(1)
        self.assertAlmostEqual(result,math.e,places=2)

    def test_exp_negative(self):
        result = MyCalculator.exp(-1)
        self.assertAlmostEqual(result,1/math.e,places=2)

    def test_exp_zero(self):
        result = MyCalculator.exp(0)
        self.assertAlmostEqual(result,1,places=2)


    def test_exp_non_numeric(self):
        with self.assertRaises(ValueError):
            MyCalculator.exp("hello")

    #### sine inverse test cases
    def test_asin_positive(self):
        result = MyCalculator.asin(1)
        self.assertAlmostEqual(result,90,places=5)
    
    def test_asin_negative(self):
        result = MyCalculator.asin(-1)
        self.assertAlmostEqual(result,-90,places=5)

    def test_asin_zero(self):
        result = MyCalculator.asin(0)
        self.assertAlmostEqual(result,0,places=5)

    def test_asin_non_numeric(self):
        with self.assertRaises(ValueError):
            MyCalculator.asin("hello")
    
    def test_asin_invalid(self):
        with self.assertRaises(ValueError):
            MyCalculator.asin(2)

    #### cosine inverse test cases.
    def test_acos_positive(self):
        result = MyCalculator.acos(0.5)
        self.assertAlmostEqual(result,60,places=5)
    
    def test_acos_negative(self):
        result = MyCalculator.acos(-1)
        self.assertAlmostEqual(result,180,places=5)

    def test_acos_zero(self):
        result = MyCalculator.acos(0)
        self.assertAlmostEqual(result,90,places=5)

    def test_acos_non_numeric(self):
        with self.assertRaises(ValueError):
            MyCalculator.acos("hello")

    def test_acos_invalid(self):
        with self.assertRaises(ValueError):
            MyCalculator.acos(-2)

    #### tangent inverse test cases.
    def test_atan_positive(self):
        result = MyCalculator.atan(1.732)
        self.assertAlmostEqual(result,60,places=2)
    
    def test_atan_negative(self):
        result = MyCalculator.atan(-1)
        self.assertAlmostEqual(result,-45,places=5)

    def test_atan_zero(self):
        result = MyCalculator.atan(0)
        self.assertAlmostEqual(result,0,places=5)

    def test_atan_non_numeric(self):
        with self.assertRaises(ValueError):
            MyCalculator.atan("hello")


    #### sine hyperbolic test cases
    def test_sinh_positive(self):
        result = MyCalculator.sinh(1)
        self.assertAlmostEqual(result,1.1752,places=4)
    
    def test_sinh_negative(self):
        result = MyCalculator.sinh(-1)
        self.assertAlmostEqual(result,-1.1752,places=4)

    def test_sinh_zero(self):
        result = MyCalculator.sinh(0)
        self.assertAlmostEqual(result,0,places=5)

    def test_sinh_non_numeric(self):
        with self.assertRaises(ValueError):
            MyCalculator.sinh("hello")



    #### cosine hyperbolic test cases
    def test_cosh_positive(self):
        result = MyCalculator.cosh(1)
        self.assertAlmostEqual(result,1.543,places=3)
    
    def test_cosh_negative(self):
        result = MyCalculator.cosh(-1)
        self.assertAlmostEqual(result,1.543,places=3)

    def test_cosh_zero(self):
        result = MyCalculator.cosh(0)
        self.assertAlmostEqual(result,1,places=5)

    def test_cosh_non_numeric(self):
        with self.assertRaises(ValueError):
            MyCalculator.cosh("hello")


    #### tangent hyperbolic test cases
    def test_tanh_positive(self):
        result = MyCalculator.tanh(1)
        self.assertAlmostEqual(result,0.7615,places=3)
    
    def test_tanh_negative(self):
        result = MyCalculator.tanh(-1)
        self.assertAlmostEqual(result,-0.7615,places=3)

    def test_tanh_zero(self):
        result = MyCalculator.tanh(0)
        self.assertAlmostEqual(result,0,places=5)

    def test_tanh_non_numeric(self):
        with self.assertRaises(ValueError):
            MyCalculator.tanh("hello")





if __name__ == '__main__':
    unittest.main()