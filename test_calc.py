import unittest
import calc

def test_calc(self):
    self.assertEqual(calculator.add(5, 10), 15)
    self.assertEqual(calculator.sub(5, 10), -5)
    self.assertEqual(calculator.mul(5, 10), 50)
    self.assertAlmostEqual(calculator.div(5, 10), .5)

if __name__ == "__main__":
    unittest.main()