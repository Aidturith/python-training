# -*- coding: utf-8 -*-

import pytest

from utils.random_pass.random_password import RandomPassword
from utils.random_pass.random_password import VALID_CHARSET
from utils.random_pass.random_password import NUMBER, LETTER_MAJ

@pytest.fixture()
def simple_pattern():
    return 'test'

def test__pattern_is_valid__simple():
    randp = RandomPassword()
    pattern = u'C'
    assert randp._pattern_validation(pattern) == None

def test__pattern_is_valid__complexe():
    randp = RandomPassword()
    pattern = u'CcVvLlpn'
    assert randp._pattern_validation(pattern) == None

def test__pattern_is_valid__fail():
    randp = RandomPassword()
    pattern = u'a'
    with pytest.raises(LookupError):
        randp._pattern_validation(pattern)

def test__pattern_is_valid__fail2():
    randp = RandomPassword()
    pattern = u'Ca'
    with pytest.raises(LookupError):
        randp._pattern_validation(pattern)


def test__get_charset_len__1():
    randp = RandomPassword()
    pattern = u'CV'
    assert randp._get_charset_len(pattern) == 26

def test__get_charset_len__2():
    randp = RandomPassword()
    pattern = u'CVLn'
    assert randp._get_charset_len(pattern) == 36


def test__get_password__len():
    randp = RandomPassword()
    pattern = u'Cvcvnnnn'
    assert len(randp._get_password(pattern)) == 8

def test__get_password__numbers():
    randp = RandomPassword()
    pattern = u''
    
    for n in range(0, 100) : pattern += u'n'
    password = randp._get_password(pattern)
    for char in password : assert char in VALID_CHARSET[NUMBER]

def test__get_password__letters():
    randp = RandomPassword()
    pattern = u''
    
    for n in range(0, 100) : pattern += u'L'
    password = randp._get_password(pattern)
    for char in password : assert char in VALID_CHARSET[LETTER_MAJ]


def test__get_entropy__1():
    randp = RandomPassword()
    pattern = u'nnnn'
    assert randp.get_entropy(pattern) == 13

def test__get_entropy__2():
    randp = RandomPassword()
    pattern = u'Lln'
    assert randp.get_entropy(pattern) == 18



