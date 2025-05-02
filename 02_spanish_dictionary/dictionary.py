def create_delimeter():
     print('-' * 50)

def create_dictionary():
    """
    The while loop keeps asking the user to enter an English word, or type "stop" to finish.
    If the word isn't already in the dictionary, the program asks the user to type its Spanish translation.
    Then it saves the English word as a key and the Spanish word as its value in the dictionary.
    If the word is already in the dictionary, the program tells the user and asks for a new word instead.

    Returns:
        Dictionary: This dictionary contains all the words added by the user as a key and their meaning in spanish as a value.
    """
    my_dictionary = {}

    while True:
        create_delimeter()
        english_word = input('🧑‍🎓 Enter a word or type "stop" to stop adding new words: ').lower()

        if english_word == 'stop':
            break
            
        if english_word not in my_dictionary:
            spanish_word = input(f'Please translate {english_word} in spanish: ')
            my_dictionary[english_word] = spanish_word
        else:
            create_delimeter()
            print('📣 This word already exist, please add another one.')
            continue
    
    return my_dictionary

user_dictionary = create_dictionary()

correct_answers = 0
wrong_answers = 0

for english_word, translation in user_dictionary.items():
        user_translation = input(f'What does {english_word} mean in spanish? ').lower()
        create_delimeter()

        if user_translation == translation:
            correct_answers += 1

            print("📖 Great, that's right!")
            create_delimeter()
        else:
             wrong_answers += 1
             print("🙇 I'm sorry, your answer is wrong!")
             create_delimeter()

print(f'You learned {correct_answers} new words, and you have to learn {wrong_answers} more.')

