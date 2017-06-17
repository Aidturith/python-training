'''
Created on 15 juin 2017

@author: Kenji
'''

from dp_gof.singleton.animals.animal import Animal

class Bear(Animal):
    '''
    A big bear!
    '''

    def __init__(self):
        self.sfx = "guoo"

print(Bear().poke())
