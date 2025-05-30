print("🔍 CHECK CHARACTER 🔍")

while True:
    char = input("\nEnter a character or (exit): ").strip()

    if char.lower() == 'exit':
        print("\n👋 Goodbye!")
        break

    if len(char) != 1:
        print("\n🙏 Please enter a single character 🙏")
        continue

    if char.isalpha():
        print(f"\n🔤 {char} is a letter! 🔤")
    elif char.isdigit():
        print(f"\n🔢 {char} is a number! 🔢")
    else:
        print(f"\n🔣 {char} is a special character! 🔣")