import unittest
from converter import Converter


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.obj = Converter()

    def test_convert_length(self):
        self.assertEqual(self.obj._convert_length(10, "km", "m"), 10_000)

    def test_convert_degrees(self):
        self.assertEqual(self.obj._convert_degrees(10, "c", "f"), 50)

    def test_convert_weight(self):
        self.assertEqual(self.obj._convert_weight(10, "kg", "gm"), 10_000)


if __name__ == "__main__":
    unittest.main()
