'''
Created on 15 juin 2017

@author: Kenji
'''

from dp_gof.singleton.animals.animal import Animal

class Cat(Animal):
    '''
    A cat!
    '''

    def __init__(self):
        self.sfx = "nya nya"
