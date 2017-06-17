'''
Created on 15 juin 2017

@author: Kenji
'''

from dp_gof.singleton.animals.animal import Animal

class Dog(Animal):
    '''
    A dog!
    '''

    def __init__(self):
        self.sfx = "wan wan"
