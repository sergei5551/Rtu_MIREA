class Converter:
    def __init__(self) -> None:
        self.converters = {
            "length": self._convert_length,
            "degrees": self._convert_degrees,
            "weight": self._convert_weight,
        }

    def convert(self, category, value, from_unit, to_unit):
        if category in self.converters:
            fanction = self.converters[category]
            return fanction(value, from_unit, to_unit)
        else:
            raise ValueError("Такой категории не существует.")

    def _convert_length(self, value, from_unit, to_unit):
        length = {
            "mm": 0.001,
            "cm": 0.01,
            "dm": 0.1,
            "m": 1.0,
            "dam": 10.0,
            "gm": 100.0,
            "km": 1000.0,
        }
        if from_unit not in length or to_unit not in length:
            return "Единица измерения не найдена"
        return value * length[from_unit] / length[to_unit]

    def _convert_degrees(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value

        if from_unit == "c":
            return (value * 9 / 5) + 32
        elif from_unit == "f":
            return (value - 32) * 5 / 9
        else:
            return "Единица измерения не найдена"

    def _convert_weight(self, value, from_unit, to_unit):
        weight = {"gm": 0.001, "kg": 1.0, "h": 100.0, "t": 1000.0}
        if from_unit not in weight or to_unit not in weight:
            return "Единица измерения не найдена"
        return value * weight[from_unit] / weight[to_unit]


def main():
    conv = Converter()
    print(f"С: {10} -> F: {conv.convert('degrees', 10, 'c', 'f')}")
    print(f"km: {100} -> m: {conv.convert('length', 100, 'km', 'dm')}")


if __name__ == "__main__":
    main()
