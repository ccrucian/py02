class OutOfRangeTemp(Exception):

    """to explain what it is, T out of range too high"""
    pass


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(temp_str: str) -> None:

    try:
        print(f"Input data is '{temp_str}'")
        temp_int: int = input_temperature(temp_str)

        if temp_int > 100:
            raise OutOfRangeTemp(f"Temperature {temp_int}"
                                 f"out of range!")
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
    test_temperature("200")


if __name__ == "__main__":
    main()
