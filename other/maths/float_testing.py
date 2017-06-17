'''
Created on 22 avr. 2016

@author: aidturith
'''

import math
from decimal import Decimal


tr_price = 9.58
string_list = str(tr_price).split('.')
str_price = '{}{:1<10}'.format(string_list[0], string_list[1][0:10])

print(str_price)

print(tr_price)
print(str(tr_price))
print('{:0<10}'.format(tr_price))


# float test
float_test = 1.5000001
print(float_test)
print(Decimal(float_test))
print(math.ceil(float_test))
print(math.floor(float_test))
print(math.trunc(float_test))

print(str(float_test))
print(repr(float_test))

float_test2 = Decimal('1.5000001')
print(float_test2 + 1)

float_test3 =  0.1 + 0.1 + 0.1 - 0.3
print(float_test3)

print("Done!")
