import unittest
import calc

class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(5, 10), 15)
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(1, 1), 3) #should fail
    def test_sub(self):
        self.assertEqual(calc.sub(5, 10), -5)
        self.assertEqual(calc.sub(10, 5), 5)
        self.assertEqual(calc.sub(10, 5), 6) #should fail
    def test_mul(self):
        self.assertEqual(calc.mul(5, 10), 50)
        self.assertEqual(calc.mul(10, 5), 50)
        self.assertEqual(calc.mul(-5, -5), 25)
        self.assertEqual(calc.mul(-5, 5), 25) #should fail
    def test_div(self):
        self.assertAlmostEqual(calc.div(5, 10), .5)
        self.assertEqual(calc.div(10, 5), 2)
        self.assertEqual(calc.div(15, 15), 1)
        self.assertEqual(calc.div(5, 10), .51) #should fail

if __name__ == "__main__":
    unittest.main(verbosity=2)