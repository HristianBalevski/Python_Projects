def get_user_inputs() -> float:
    while True:
        try:
            first_number = float(input("\nEnter the first number: "))
            second_number = float(input("Enter the second number: "))

            return first_number, second_number
        except ValueError:
            print("\n❗❗❗ Please enter a valid number..." + "\n")