# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
from random import randint
import requests

class Game():
    """ A simple word game """
    def __init__(self):
        """ Initialize grid with 9 letters """
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.grid = [letters[randint(0, len(letters) - 1)] for index in range(9)]
    def is_valid(self, word):
        """ Test wether or not a word is valid considering s specific grid """
        result = True
        if self.__check_dictionary(word):
            print(f'Word {word} is not in the dictionnary...')
            result = False
        else:
            for char in word:
                if char in self.grid:
                    result = False
        return result
    def __check_dictionary(self, word):
        r = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        print(r)
        response = r.json()
        return response['found']