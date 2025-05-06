from change_role import change_user_role
from display_people import display_all_people
from check_for_available_people import run_if_people_exist
from celebrate_birthday import celebrate_user_birthday
from remove_user import remove_existing_user
from add_person import add_new_person
import itertools

MIN_NAME_LENGTH = 3
MAX_NAME_LENGTH = 25
MIN_AGE = 18
MAX_AGE = 68

id_generator = itertools.count(1)


def get_user_id():
    user_id = int(input("Enter user 🆔: "))

    return user_id


print("\n👨‍💼 ----- MANAGE PEOPLE SMARTLY ----- 👨‍💼")

available_people = {}

allowed_roles = [
    "Student",
    "Engineer",
    "Director",
    "Team Leader",
    "Supervisor",
    "Web Developer",
]

while True:

    print(
        "\nPlease choose a number (1-6) 🔢\n"
        "\nPress 1 to see all people 👀"
        "\nPress 2 to add new person 👨‍💼"
        "\nPress 3 to celebrate birthday 🥳"
        "\nPress 4 to change a person role 🔄"
        "\nPress 5 to remove a person ❌"
        "\nPress 6 to leave the program 🚪"
    )

    try:
        user_input = int(input("\nWhat's your number?: "))
    except ValueError:
        print("\nPlease enter a valid number!")
        continue

    if user_input < 1 or user_input > 6:
        print("\n🔢 Please enter a number between 1 - 6 🔢")
        continue

    if user_input == 1:
        display_all_people(available_people)

    elif user_input == 2:
        add_new_person(
            available_people,
            id_generator,
            allowed_roles,
            MIN_NAME_LENGTH,
            MAX_NAME_LENGTH,
            MIN_AGE,
            MAX_AGE,
        )

    elif user_input == 3:
        run_if_people_exist(
            available_people, lambda: celebrate_user_birthday(available_people)
        )

    elif user_input == 4:
        run_if_people_exist(
            available_people, lambda: change_user_role(available_people, allowed_roles)
        )

    elif user_input == 5:
        run_if_people_exist(
            available_people, lambda: remove_existing_user(available_people)
        )

    elif user_input == 6:
        print("Goodbye 👋")
        break
