from operations import add, subtract, multiply, divide
from input_handler import get_user_inputs

def main():
    print("\n🧮 SIMPLE CALCULATOR 🧮")

    while True:
        print("\nPlease choose a number between 1 and 5: " + "\n")
        print("1. Add ➕")
        print("2. Subtract ➖")
        print("3. Multiply ✖️")
        print("4. Divide ➗")
        print("5. Exit 🚪")

        try:
            user_input = int(input("\nEnter a number: "))
        except ValueError:
            print("\n❌That is not a valid input, try again...")
            continue

        valid_inputs = [1, 2, 3, 4, 5]

        if user_input not in valid_inputs:
            print("\n❌ Invalid input, try again...")
            continue

        if user_input == 5:
            print("\nGoodbye 👋")
            break

        first_number, second_number = get_user_inputs()

        operations = {
            1: ("Add", add),
            2: ("Subtract", subtract),
            3: ("Multiply", multiply),
            4: ("Divide", divide),
        }

        operation_name, operation_function = operations[user_input]

        try:
            result = operation_function(first_number, second_number)
            print(f"\n📊 The result of {operation_name.lower()} is: {result:.2f}")
        except ZeroDivisionError as e:
            print(f"\n⚠️ {e}")


if __name__ == "__main__":
    main()