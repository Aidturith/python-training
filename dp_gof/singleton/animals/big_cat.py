'''
Created on 15 juin 2017

@author: Kenji
'''

from dp_gof.singleton.animals.animal import Animal

class BigCat(Animal):
    '''
    A BIG cat!
    '''

    def __init__(self):
        self.sfx = "gaoo"
