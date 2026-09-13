class OutOfRange(Exception):
    """when out of optimal range"""
    pass


class TooHot(Exception):
    """too hot"""
    pass


class TooCold(Exception):
    """too cold for plants"""
    pass


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)

    if (-50 <= temp <= 0) or (40 <= temp <= 200):
        raise OutOfRange("Temp is out optimal range")
    return temp


def test_temperature(temp_str: str) -> None:

    try:
        print(f"Input data is '{temp_str}'")
        temp_int: int = input_temperature(temp_str)

        if temp_int > 200:
            raise TooHot(f"Temp {temp_int}°C too hot for plants"
                         f" (max 40°C)")
        elif temp_int < -50:
            raise TooCold(f"Temp {temp_int}°C too cold for plants"
                          f" (max 0°C)")

    except TooHot as e:
        print(f"{e}")
    except TooCold as e:
        print(f"{e}")
    except OutOfRange as e:
        print(f"Caught an optimum error: {e}")
    except Exception as e:
        print(f"Caught input_temp error: {e}")
    else:
        print(f"Temperature is now {temp_int}°C")
    finally:
        print("All tests completed - program "
              "didn't crash!")


def main() -> None:

    print("=== Garden Temperature ===")
    print("")

    test_temperature("25")
    print("")
    test_temperature("abc")
    print("")
    test_temperature("50")
    print("")
    test_temperature("250")


if __name__ == "__main__":
    main()
