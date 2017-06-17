'''
Created on 15 juin 2017

@author: Kenji
'''

import time

from dp_gof.singleton.animals.animal import Animal
from dp_gof.singleton.animals.big_cat import BigCat
from dp_gof.singleton.animals.pig import Pig


def test_animal():
    ani = Animal("hello world")
    assert ani.poke() == "hello world"

def test_big_cat():
    big_cat = BigCat()
    assert big_cat.poke() == "gaoo"

def test_pig_live():
    pig = Pig()
    
    start_t = time.time()
    pig.live()
    assert (time.time() - start_t) <= (pig.expectancy * pig.MAX_WAIT_TIME)
