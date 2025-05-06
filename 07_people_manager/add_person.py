from validate_name import validate_name
from validate_age import get_valid_age
from validate_role import get_valid_role


def add_new_person(
    people: dict[int, dict],
    id_generator,
    allowed_roles: list[str],
    min_name_length: int,
    max_name_length: int,
    min_age: int,
    max_age: int,
) -> None:
    """
    Prompts the user to input a new person's name, age, and role, validates the input,
    and adds the person to the provided people dictionary using a unique ID.

    This function performs the following steps:
    - Asks the user for a name and validates it based on alphabetic characters and length.
    - Prompts for age and role, validating both according to the specified constraints.
    - Generates a unique ID using the provided id_generator.
    - Adds the validated person to the people dictionary with the generated ID.

    Parameters:
        people (dict[int, dict]): The dictionary where new people are stored.
        id_generator (Iterator[int]): An iterator that produces unique integer IDs.
        allowed_roles (list[str]): A list of valid roles to choose from.
        min_name_length (int): The minimum length allowed for a name.
        max_name_length (int): The maximum length allowed for a name.
        min_age (int): The minimum allowed age.
        max_age (int): The maximum allowed age.

    Returns:
        None
    """

    while True:
        name = input("\nEnter a name: ").strip().title()

        if not validate_name(name):
            print(
                f"The name must contain only letters a-z 🔠"
                f"min length {min_name_length} and max length {max_name_length}"
            )
            continue

        valid_age = get_valid_age(min_age, max_age)
        valid_role = get_valid_role(allowed_roles)
        new_id = next(id_generator)

        people[new_id] = {"name": name, "age": valid_age, "role": valid_role.title()}

        print(f"\n✅ {name} is now part of the company and their ID is {new_id}.")
        break
