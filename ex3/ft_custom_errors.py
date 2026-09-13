class GardenError(Exception):
    """basic error for garden problem"""
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    """problems with plants"""
    pass


class WaterError(GardenError):
    """problems with watering"""
    pass


def sensor(plant: str, water: int, wilt: bool) -> None:
    print("Testing PlantError...")
    if wilt:
        try:
            raise PlantError(f"The {plant} is wilting!")
        except PlantError as e:
            print(f"Caught PlantError: {e}")
    print("Testing WaterError...")
    if water < 50:
        try:
            raise WaterError("Not enough water in the tank!")
        except WaterError as e:
            print(f"Caught WaterError: {e}")
    print("Testing catching all garden errors...")
    if wilt and water < 50:
        try:
            raise PlantError(f"The {plant} is wilting!")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        try:
            raise WaterError("Not enough water in the tank!")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print("")
    print("All custom error types work correctly!")


def main() -> None:
    sensor("tomato", 10, True)


if __name__ == "__main__":
    main()
