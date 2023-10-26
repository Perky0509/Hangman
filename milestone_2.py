import random


word_list = ('melon', 'grapes', 'strawberries', 'figs', 'kiwi')

class GuessTheWord:
        
    def __init__(self, word_list = []):
        self.word_list = word_list 
    
    def word_options(self):
        return self.word_list

    def random_word(self): 
        word = random.choice(self.word_list)
        return word

    def user_guess(self): 
        guess = input()
        print(f'Please enter a single letter:', guess)
        if len(guess) == 1 and guess.isalpha():
            return "Good guess!"
        else:
            return "oops! That is not a valid input."
           

first_list = GuessTheWord(['melon', 'grapes', 'strawberries', 'figs', 'kiwi'])

print(first_list.word_options())
print(first_list.random_word())
print(first_list.user_guess())

