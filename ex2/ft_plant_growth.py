#!/usr/bin/env python3


class Plant:

    # I created this standard growth rate for each plant type
    growth_rates = {"rose": 0.8, "sunflower": 1.5, "cactus": 0.1}

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

    def age(self) -> None:
        self.age_days += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, "
              f"{self.age_days} days old")


def main() -> None:
    rose = Plant("Rose", 25.0, 30)

    print("=== Garden Plant Growth ===")
    rose.show()

    initial_height = rose.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")

        rose.grow()
        rose.age()
        rose.show()

    growth_this_week = round(rose.height - initial_height, 1)
    print(f"Growth this week: {growth_this_week}cm")


if __name__ == "__main__":
    main()
