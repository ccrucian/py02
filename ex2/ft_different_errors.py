def garden_operations(operation_number: int) -> None:

    if operation_number == 0:
        operation_number = int("abc")
    elif operation_number == 1:
        operation_number /= 0
    elif operation_number == 2:
        open("file.txt")
    elif operation_number == 3:
        "abc" + operation_number
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    for i in range(5):

        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print("All error types tested successfully!")


def main() -> None:

    print("=== Garden Error Types Demo ===")
    print("")
    test_error_types()


if __name__ == "__main__":
    main()
