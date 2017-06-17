'''
Created on 15 juin 2017

@author: Kenji
'''

from multiprocessing.pool import ThreadPool

from dp_gof.singleton.animals.pig import Pig
from dp_gof.singleton.animals.cat import Cat
from dp_gof.singleton.animals.bear import Bear
from dp_gof.singleton.animals.dog import Dog


class Farm(object):
    '''
    A farm, with animals..
    '''
    
    pool_size = 0
    animals = []
    
    # singleton
    instance = None
    
    def __new__(cls, pool_size=4):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        
        cls.instance.pool_size = pool_size
        return cls.instance
    
    
    def setup_farm(self, newcomer):
        self.animals.append(newcomer)
    
    def start_farm(self):
        pool = ThreadPool(self.pool_size)
        #pool.map([animal.live() for animal in self.animals])
        pool.map(lambda animal: animal.live(), self.animals)
        
        pool.close()
        pool.join()


st_farm = Farm(2)
st_farm.setup_farm(Pig())
st_farm.setup_farm(Cat())
st_farm.setup_farm(Bear())
st_farm.setup_farm(Dog())

print(st_farm is Farm(3))
st_farm.start_farm()
print(st_farm is Farm(5))
