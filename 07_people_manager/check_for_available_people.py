from typing import Callable, Dict, Any


def run_if_people_exist(people: Dict[int, Dict[str, Any]], action: Callable) -> None:
    """
    Executes a given action only if the people dictionary is not empty.

    This function checks whether any people are currently stored. If the dictionary
    is empty, it prints a message and exits early. If people exist, it executes
    the provided action function.

    Parameters:
        people (Dict[int, Dict[str, Any]]): A dictionary mapping user IDs to personal
        details such as 'name', 'age', and 'role'.
        action (Callable): A zero-argument function to be executed if people exist.

    Returns:
        None
    """

    if not people:
        print("\n🚷 No people in the company, please add at least one. 🚷")
        return
    action()
