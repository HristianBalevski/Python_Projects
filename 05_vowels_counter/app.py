user_input = input("🔠 Enter a word or a sentence: ")

def count_vowels(text: str) -> str:
    total_vowels = len([vowel for vowel in text.lower() if vowel in ['a', 'u', 'e', 'i', 'o', 'y']])
    return f"🧮 The total vowels in your text are {total_vowels} ✅"

print(count_vowels(user_input))