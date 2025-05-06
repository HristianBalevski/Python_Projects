def validate_name(name: str) -> bool:
    """
    Validates whether the given name contains only alphabetic characters (including
    international letters) and spaces, and checks if its length is within the allowed range.

    The name must be between 3 and 30 characters in total, including spaces. All characters
    (excluding spaces) must be alphabetic, allowing for names with accented or non-ASCII
    characters (e.g., Émilie, José, Čavdar, Łukasz). Numbers, symbols, and special characters
    are not allowed.

    Parameters:
        name (str): The name to validate.

    Returns:
        bool: True if the name is valid, False otherwise.
    """

    name = name.strip()
    cleaned_name = name.replace(" ", "")

    return all(char.isalpha() for char in cleaned_name) and 3 <= len(name) <= 30
