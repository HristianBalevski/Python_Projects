import random

print("🏫 WELCOME TO OUR LIBRARY 🏫")

def create_delimeter():
    print("-" * 30)

def print_empty_row():
    print()

create_delimeter()


def get_fantasy_book() -> dict[str, list]:
    fantasy_library = {
        "J.R.R. Tolkien": [
            "The Hobbit",
            "The Fellowship of the Ring",
            "The Return of the King",
        ],
        "J.K. Rowling": [
            "Harry Potter and the Sorcerer’s Stone",
            "Harry Potter and the Prisoner of Azkaban",
            "Harry Potter and the Deathly Hallows",
        ],
        "George R.R. Martin": [
            "A Game of Thrones",
            "A Clash of Kings",
            "A Storm of Swords",
        ],
    }

    return fantasy_library


def get_science_book() -> dict[str, list]:

    science_library = {
        "Isaac Asimov": ["Foundation", "I, Robot", "The Caves of Steel"],
        "Philip K. Dick": [
            "Do Androids Dream of Electric Sheep?",
            "Ubik",
            "The Man in the High Castle",
        ],
        "Arthur C. Clarke": [
            "2001: A Space Odyssey",
            "Childhood’s End",
            "Rendezvous with Rama",
        ],
    }

    return science_library


def get_mystery_book() -> dict[str, list]:
    mystery_library = {
        "Agatha Christie": [
            "Murder on the Orient Express",
            "And Then There Were None",
            "The Murder of Roger Ackroyd",
        ],
        "Arthur Conan Doyle": [
            "A Study in Scarlet",
            "The Hound of the Baskervilles",
            "The Sign of Four",
        ],
        "Stieg Larsson": [
            "The Girl with the Dragon Tattoo",
            "The Girl Who Played with Fire",
            "The Girl Who Kicked the Hornet's Nest",
        ],
    }

    return mystery_library


def get_romance_book() -> dict[str, list]:
    romance_library = {
        "Jane Austen": ["Pride and Prejudice", "Sense and Sensibility", "Emma"],
        "Nicholas Sparks": ["The Notebook", "A Walk to Remember", "Dear John"],
        "Nora Roberts": ["Vision in White", "The Witness", "The Next Always"],
    }

    return romance_library


def get_history_book() -> dict[str, list]:
    history_library = {
        "Ken Follett": [
            "The Pillars of the Earth",
            "World Without End",
            "Fall of Giants",
        ],
        "Hilary Mantel": [
            "Wolf Hall",
            "Bring Up the Bodies",
            "The Mirror and the Light",
        ],
        "Philippa Gregory": [
            "The Other Boleyn Girl",
            "The White Queen",
            "The Constant Princess",
        ],
    }

    return history_library

def show_autors_and_books_for_choosen_genre(choosen_genre_data: dict[str, list]) -> str:
    author = random.choice(list(choosen_genre_data.keys()))
    book = random.choice(choosen_genre_data[author])

    return f"Why don't you try 📗 {book} 📗 by {author}❓"
        

genre_mapper = {
    "Fantasy": get_fantasy_book(),
    "Science Fiction": get_science_book(),
    "Mystery": get_mystery_book(),
    "Romance": get_romance_book(),
    "Historical Fiction": get_history_book(),
}
print("What genre do you like❓")
print()

for index, genre in enumerate(genre_mapper):
    print(f"{index + 1}. {genre}")

while True:
    create_delimeter()
    user_genre_choice = input("🎬 Choose a genre 🎬 or type 'Exit' to leave the library: ").title()
    print_empty_row()

    if user_genre_choice == 'Exit':
        print("👋 Goodbye!")
        break
    elif user_genre_choice not in genre_mapper:
        print(f"💔 Your genre is not available, please choose one of these: {", ".join(list(genre_mapper.keys()))} 🔍")
    else:
        genre_data =  genre_mapper[user_genre_choice]
        print(show_autors_and_books_for_choosen_genre(genre_data))
        break