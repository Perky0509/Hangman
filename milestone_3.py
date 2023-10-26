import random


word_list = ['melon', 'grapes', 'strawberries', 'figs', 'kiwi']
                
def check_user_guess(user_letter_guess):
    random_word = random.choice(word_list)
    if user_letter_guess in random_word:
        print(f"Good guess! {user_letter_guess} is in the word.")
    else: 
        print(f"Sorry, {user_letter_guess} is not in the word. Try again.")
    return random_word


def ask_for_input():
    while True:
        user_letter_guess = input(f'Please enter a single letter:')
        if len(user_letter_guess) != 1 and user_letter_guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        else:
            break 
        return check_user_guess(user_letter_guess)
      
word_list = ['melon', 'grapes', 'strawberries', 'figs', 'kiwi']
ask_for_input()

