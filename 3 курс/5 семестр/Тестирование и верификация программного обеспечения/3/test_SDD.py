import unittest
from converter import Converter


class TestConverter(unittest.TestCase):
    def test_convert_degrees(self):
        convr = Converter()
        result = convr.convert("degrees", 10, "c", "f")
        assert result == 50

    def test_convert_length(self):
        convr = Converter()
        result = convr.convert("length", 100, "km", "dm")
        assert result == 1_000_000

    def test_convert_weight(self):
        convr = Converter()
        result = convr.convert("weight", 1500, "gm", "h")
        assert result == 0.015


if __name__ == "__main__":
    unittest.main()
