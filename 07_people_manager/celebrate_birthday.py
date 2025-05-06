from check_for_id import get_existing_user_id
from typing import Dict, Any


def celebrate_user_birthday(people: Dict[int, Dict[str, Any]]) -> None:
    """
    Increases the age of a selected person by one year to celebrate their birthday.

    Prompts the user to enter a valid user ID from the provided people dictionary.
    If the ID exists, the corresponding person's age is incremented by one, and
    a celebratory message is printed to the console.

    Parameters:
        people (Dict[int, Dict[str, Any]]): A dictionary of people where the key is
        a unique user ID and the value is a dictionary containing user details such
        as 'name', 'age', and 'role'.

    Returns:
        None
    """

    print("\n🎉 BIRTHDAY MODE 🎉")
    user_id = get_existing_user_id(people)
    people[user_id]["age"] += 1
    print(f"\n🥳 Happy birthday {people[user_id]['name']}! 🥳")
