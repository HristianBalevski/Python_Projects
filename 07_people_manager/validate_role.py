def get_valid_role(roles: list[str]) -> str:
    """
    Prompts the user to select a valid role from a predefined list.

    Continuously displays the available roles and asks for input until the user
    provides a valid role. Input is normalized using `.strip().title()` to allow
    flexible user input (e.g., "web developer" becomes "Web Developer").

    Parameters:
        roles (list[str]): A list of valid role names to choose from.

    Returns:
        str: The selected role, guaranteed to be one of the allowed options.
    """

    while True:
        print("\nChoose a role:\n" + "\n" + "\n".join(roles))
        role = input("\nRole: ").strip().title()

        if role in roles:
            return role

        print("\n❌ Invalid role. Try again.")
