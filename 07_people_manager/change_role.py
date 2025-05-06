from check_for_id import get_existing_user_id
from validate_role import get_valid_role
from typing import Dict, Any


def change_user_role(people: Dict[int, Dict[str, Any]], roles: list[str]) -> None:
    """
    Prompts the user to change the role of an existing person in the system.

    The function asks for a valid user ID and a new role from the list of allowed roles.
    If the selected new role is different from the person's current role, the change is
    applied and a confirmation message is printed. If the new role is the same, the user
    is prompted to try again.

    Parameters:
        people (Dict[int, Dict[str, Any]]): A dictionary mapping user IDs to personal
        details, including 'name', 'age', and 'role'.
        roles (list[str]): A list of valid roles that users can be assigned to.

    Returns:
        None
    """

    print("\n🔄 CHANGE ROLE 🔄")
    user_id = get_existing_user_id(people)

    while True:
        old_role = people[user_id]["role"]
        new_role = get_valid_role(roles)

        if old_role != new_role:
            people[user_id]["role"] = new_role
            print(
                f"\n🔄 {people[user_id]["name"]} transitioned from a {old_role} to {new_role} 🔄"
            )
            break
        else:
            print("\n🎭 The new role should differ from the old one! 🎭")
