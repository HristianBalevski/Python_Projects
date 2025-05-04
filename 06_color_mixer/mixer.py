print("🎨 WELCOME TO COLOR MIXER 🎨")

mixer = {
    ("red", "blue"): "🟣 Purple 🟣",
    ("blue", "yellow"): "🟢 Green 🟢 ",
    ("red", "yellow"): "🟠 Orange 🟠",
    ("blue", "white"): "🩵 Light Blue 🩵 ",
    ("red", "white"): "🩷 Pink 🩷",
    ("green", "yellow"): "🍋‍🟩 Lime Green 🍋‍🟩",
    ("black", "white"): "🩶 Gray 🩶",
    ("red", "black"): "🩸 Maroon 🩸",
    ("blue", "green"): "🩵 Teal 🩵",
    ("purple", "white"): "🪻 Lavender 🪻",
}

while True:
    first_color = input("Enter your first color or 'exit': ").lower()

    if first_color == "exit":
        break

    second_color = input("Enter your second color or 'exit': ").lower()

    if second_color == "exit":
        break

    pair = (first_color, second_color)
    reversed_pair = (second_color, first_color)

    result = mixer.get(pair) or mixer.get(reversed_pair)

    if result:
        print(
            f"\nWhen you mix {first_color} and {second_color}, you get {result}"
        )
    else:
        print("\n🎨 I do not know what color this is. 🎨")

    print("-" * 40)
    print("Try another mix if you want.")
