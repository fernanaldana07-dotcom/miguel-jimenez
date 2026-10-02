import unittest
from app import sumar, restar

class TestCalculadora(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)

    def test_restar(self):
        # Esta comprobacion fallara porque 5 - 2 dara 7 en lugar de 3
        self.assertEqual(restar(5, 2), 3)

if __name__ == "__main__":
    unittest.main()
