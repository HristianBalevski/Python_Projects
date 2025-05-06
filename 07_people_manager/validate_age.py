def get_valid_age(min_age: int, max_age: int) -> int:
    """
    Prompts the user to enter a valid age within the specified range.

    Continuously requests input until the user provides an integer within the given
    minimum and maximum age boundaries. Displays error messages for invalid input types
    or values outside the accepted range.

    Parameters:
        min_age (int): The minimum acceptable age.
        max_age (int): The maximum acceptable age.

    Returns:
        int: A valid age value between min_age and max_age (inclusive).
    """

    while True:
        try:
            age = int(input(f"\n🗓️ Please enter age between {min_age} - {max_age} 🗓️: "))
            if age < min_age or age > max_age:
                print("\n🚫 Invalid age range. 🚫")
                continue
            return age
        except ValueError:
            print("\n❌ Invalid number. Try again. ❌")
