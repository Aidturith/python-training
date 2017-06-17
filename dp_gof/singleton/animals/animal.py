'''
Created on 15 juin 2017

@author: Kenji
'''

import random
import time

class Animal(object):
    '''
    Simple living being!
    '''

    # wait times in seconds
    MIN_WAIT_TIME = 0
    MAX_WAIT_TIME = 3

    sfx = ""
    expectancy = 5
    

    def __init__(self, sfx="..."):
        self.sfx = sfx
    
    
    def poke(self):
        return self.sfx
    
    def live(self):
        for i in range(0, self.expectancy):
            time.sleep(random.uniform(self.MIN_WAIT_TIME, self.MAX_WAIT_TIME))
            print(self.poke())
