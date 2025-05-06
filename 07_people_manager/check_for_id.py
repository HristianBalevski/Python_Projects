from typing import Dict, Any


def get_existing_user_id(people: Dict[int, Dict[str, Any]]) -> int:
    """
    Prompts the user to enter a valid user ID from the provided people dictionary.

    This function ensures that the entered ID is an integer and exists in the people
    dictionary. It loops until the user provides a valid and existing ID, then returns it.

    Parameters:
        people (Dict[int, Dict[str, Any]]): A dictionary mapping user IDs to personal
        details such as 'name', 'age', and 'role'.

    Returns:
        int: A valid user ID that exists in the people dictionary.
    """

    while True:
        try:
            user_id = int(input("\nEnter user ID: "))
            if user_id not in people:
                print("\n🙅 User ID not found. 🙅")
                continue
            return user_id
        except ValueError:
            print("❌ Invalid ID. Try again. ❌")
