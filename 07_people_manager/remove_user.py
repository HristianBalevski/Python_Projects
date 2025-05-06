from check_for_id import get_existing_user_id
from typing import Dict, Any


def remove_existing_user(people: Dict[int, Dict[str, Any]]) -> None:
    """
    Removes a person from the system based on a valid user ID.

    Prompts the user to enter an existing user ID. If the ID is valid, the corresponding
    person is removed from the people dictionary, and a confirmation message is displayed.

    Parameters:
        people (Dict[int, Dict[str, Any]]): A dictionary mapping user IDs to personal
        details such as 'name', 'age', and 'role'.

    Returns:
        None
    """

    user_id = get_existing_user_id(people)
    name_to_be_fired = people[user_id]["name"]

    del people[user_id]
    print(f"\n😔 {name_to_be_fired} has been fired from the company! 😔")
