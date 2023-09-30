import random

word_list = ['melon', 'grapes', 'strawberries', 'figs', 'kiwi']
 

                
def check_guess(guess):
    word = random.choice(word_list)
    #guess = input(f'Please enter a single letter: {prompt}').lower()
    
    if guess in word:
        print(f"Good guess! {guess} is in the word.")

    else: 
        print(f"Sorry, {guess} is not in the word. Try again.")
    
    return word


def ask_for_input():

    while True:
        guess = input(f'Please enter a single letter:')
        if len(guess) != 1 and guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        else:
            break 
    
    return check_guess(guess)
      

word_list = ['melon', 'grapes', 'strawberries', 'figs', 'kiwi']
ask_for_input()
#check_guess(prompt)
