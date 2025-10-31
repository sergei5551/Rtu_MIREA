import unittest
from converter import Converter


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.obj = Converter()

    def test_user_weight(self):  # Кондитер хочет взвесить ингридиенты в килограммах,
        # а весы принимают только граммы
        result = self.obj.convert("weight", 0.5, "kg", "gm")
        self.assertEqual(result, 500)

    def test_user_length(self):  # Строитель хочет купить 15 м провода, а продают в дм
        result = self.obj.convert("length", 15, "m", "dm")
        self.assertEqual(result, 150)


if __name__ == "__main__":
    unittest.main()
