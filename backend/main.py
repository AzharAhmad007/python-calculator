from backend.calculator import calculate
from backend.exceptions import (
    CalculatorError,
)


def main():
    print("=== Python Calculator ===")

    while True:
        print("\nAvailable operations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("\nSelect an operation: ").strip()

        if choice == "7":
            print("Exiting calculator. Goodbye!")
            break

        operation_map = {
            "1": "add",
            "2": "subtract",
            "3": "multiply",
            "4": "divide",
            "5": "modulus",
            "6": "power",
        }

        operation = operation_map.get(choice)

        if operation is None:
            print("Invalid choice. Please try again.")
            continue

        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))

            result = calculate(a, b, operation)

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")

        except CalculatorError as error:
            print(f"Calculation error: {error}")


if __name__ == "__main__":
    main()