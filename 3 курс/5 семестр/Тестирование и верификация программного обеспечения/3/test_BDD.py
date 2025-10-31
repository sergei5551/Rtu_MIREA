import unittest
from converter import Converter


class TestConverter(unittest.TestCase):
    def test_water_boiling_temperature_conversion(self):
        # Given
        converter = Converter()
        input_value = 100
        from_unit = "c"
        to_unit = "f"

        # When
        result = converter.convert("degrees", input_value, from_unit, to_unit)

        # Then
        self.assertEqual(result, 212)


if __name__ == "__main__":
    unittest.main()
