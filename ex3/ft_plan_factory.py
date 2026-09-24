#!/usr/bin/env python3

class Plant:

    # I created this standard growth rate for each plant type
    growth_rates = {"rose": 0.8, "sunflower": 1.5, "cactus": 0.1,
                    "oak": 2.5, "fern": 0.5}

    # None allows me to use a custom rate or the standard from the table
    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float | None = None) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

        if growth_rate is None:
            growth_rate = self.growth_rates[self.name.lower()]

        self.growth_rate = growth_rate

    def grow(self) -> None:
        self.height += self.growth_rate

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {round(self.height, 1)}cm, "
              f"{self.age_days} days old")


def main() -> None:
    plants = [Plant("Rose", 25.0, 30), Plant("oAk", 200.0, 365),
              Plant("cactus", 5.0, 90), Plant("SUNFLOWER", 80.0, 45),
              Plant("FeRn", 15.0, 120)]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
