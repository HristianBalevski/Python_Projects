from typing import Dict, Any


def display_all_people(people: Dict[int, Dict[str, Any]]) -> None:
    """
    Displays all people in the system along with their ID, name, age, and role.

    If the people dictionary is empty, a message is shown indicating that there are
    no records to display. Otherwise, it prints the details of each person in a
    formatted manner.

    Parameters:
        people (Dict[int, Dict[str, Any]]): A dictionary mapping user IDs to personal
        details, including 'name', 'age', and 'role'.

    Returns:
        None
    """

    if not people:
        print("\n🤷 No people to show. 🤷")
        return

    for id, person in people.items():
        print(
            f"\nID: {id} | Name: {person['name']}, Age: {person['age']}, Role: {person['role']}"
        )
