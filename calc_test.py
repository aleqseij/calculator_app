import unittest
from calc_operations import addition, subtraction, multiplication, division, modulus, power, square_root, sine, cosine, \
    Memory


class TestCalcOperations(unittest.TestCase):

    # Тесты для базовых операций
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(subtraction(5, 3), 2)
        self.assertEqual(subtraction(2, 5), -3)

    def test_multiplication(self):
        self.assertEqual(multiplication(3, 4), 12)
        self.assertEqual(multiplication(-2, 3), -6)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        with self.assertRaises(ValueError):
            division(10, 0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(10, 5), 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)

    def test_square_root(self):
        self.assertEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(-9)

    # Тесты для тригонометрических функций
    def test_sine(self):
        self.assertEqual(sine(0), 0)
        self.assertEqual(sine(90), 1)

    def test_cosine(self):
        self.assertEqual(cosine(0), 1)
        self.assertEqual(cosine(90), 0)

    # Тестирование класса Memory
    def test_memory_operations(self):
        memory = Memory()
        memory.m_add(5)
        self.assertEqual(memory.memory, 5)
        memory.m_subtract(2)
        self.assertEqual(memory.memory, 3)
        memory.m_multiply(2)
        self.assertEqual(memory.memory, 6)
        memory.m_divide(3)
        self.assertEqual(memory.memory, 2)
        memory.m_clear()
        self.assertEqual(memory.memory, 0)

    # Тестирование ввода
    def test_invalid_decimal_input(self):
        with self.assertRaises(ValueError):
            Memory().m_add("invalid")
        with self.assertRaises(ValueError):
            division("invalid", 5)


if __name__ == '__main__':
    unittest.main()
