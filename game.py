# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
from random import randint


class Game():
    """ A simple word game """
    def __init__(self):
        """ Initialize grid with 9 letters """
        letters = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
        self.grid = [letters[randint(0, len(letters) - 1)] for index in range(9)]
