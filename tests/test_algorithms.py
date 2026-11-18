import unittest
from algorithms.naive import naive_power
from algorithms.fast_power import recursive_fast_power, iterative_fast_power
from algorithms.modular_power import modular_fast_power

class TestPowerAlgorithms(unittest.TestCase):
    def test_known_values(self):
        self.assertEqual(naive_power(2, 10), 1024)
        self.assertEqual(recursive_fast_power(2, 10), 1024)
        self.assertEqual(iterative_fast_power(2, 10), 1024)
        self.assertEqual(modular_fast_power(7, 13, 11), 2)

    def test_edge_cases(self):
        self.assertEqual(iterative_fast_power(99, 0), 1)
        self.assertEqual(recursive_fast_power(0, 5), 0)
        self.assertEqual(modular_fast_power(0, 5, 7), 0)
        self.assertEqual(modular_fast_power(10, 1, 7), 3)

    def test_against_builtin(self):
        for a in range(-4, 8):
            for e in range(0, 15):
                self.assertEqual(iterative_fast_power(a, e), pow(a, e))
                self.assertEqual(recursive_fast_power(a, e), pow(a, e))
                self.assertEqual(modular_fast_power(a, e, 13), pow(a, e, 13))

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError): iterative_fast_power(2, -1)
        with self.assertRaises(ValueError): modular_fast_power(2, 3, 1)

if __name__ == "__main__":
    unittest.main()
