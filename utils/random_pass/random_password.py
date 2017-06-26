# -*- coding: utf-8 -*-
# tools, 5 juin 2017

import string
import math
import random
import argparse

from argparse import RawTextHelpFormatter

CONSO_MAJ = u"C"
CONSO_MIN = u"c"
VOWEL_MAJ = u"V"
VOWEL_MIN = u"v"
LETTER_MAJ = u"L"
LETTER_MIN = u"l"
NUMBER = u"n"
PONCTION = u"P"
PONCTION_SMA = u"p"
VALID_CHARSET = {
    CONSO_MAJ: u"BCDFGHJKLMNPQRSTVWXZ",
    CONSO_MIN: u"BCDFGHJKLMNPQRSTVWXZ".lower(),
    VOWEL_MAJ: u"AEIOUY",
    VOWEL_MIN: u"AEIOUY".lower(),
    LETTER_MAJ: string.ascii_uppercase,
    LETTER_MIN: string.ascii_lowercase,
    PONCTION: string.punctuation,
    PONCTION_SMA: u"!\"#$%&'*+,-.:;=?@_",
    NUMBER: string.digits,
}

class RandomPassword():
    
    def _pattern_validation(self, pattern):
        for char in pattern:
            if char not in VALID_CHARSET.keys():
                raise LookupError()
    
    def _get_charset_len(self, pattern):
        charset_len = 0
        
        if CONSO_MIN in pattern and LETTER_MIN not in pattern:
            charset_len += len(VALID_CHARSET[CONSO_MIN])
        if CONSO_MAJ in pattern and LETTER_MAJ not in pattern:
            charset_len += len(VALID_CHARSET[CONSO_MAJ])
        if VOWEL_MIN in pattern and LETTER_MIN not in pattern:
            charset_len += len(VALID_CHARSET[VOWEL_MIN])
        if VOWEL_MAJ in pattern and LETTER_MAJ not in pattern:
            charset_len += len(VALID_CHARSET[VOWEL_MAJ])
        
        if LETTER_MIN in pattern:
            charset_len += len(VALID_CHARSET[LETTER_MIN])
        if LETTER_MAJ in pattern:
            charset_len += len(VALID_CHARSET[LETTER_MAJ])
        
        if NUMBER in pattern:
            charset_len += len(VALID_CHARSET[NUMBER])
        if PONCTION in pattern:
            charset_len += len(VALID_CHARSET[PONCTION])
        if PONCTION_SMA in pattern:
            charset_len += len(VALID_CHARSET[PONCTION_SMA])
        
        return charset_len
    
    def _get_password(self, pattern):
        try:
            self._pattern_validation(pattern)
        except LookupError:
            print(u"Le format n'est pas valide!")
        
        password = u''
        for char in pattern:
            for charset_key in VALID_CHARSET.keys():
                if char == charset_key:
                    password += random.SystemRandom().choice(VALID_CHARSET[charset_key])
        
        return password
    
    def get_passwords(self, pattern, iterations):
        passwords = []
        for n in range(0, iterations):
            passwords.append(self._get_password(pattern))
        return passwords
    
    def get_entropy(self, pattern):
        try:
            self._pattern_validation(pattern)
        except LookupError:
            print(u"Le format n'est pas valide!")
        
        charset_len = self._get_charset_len(pattern)
        pattern_len = len(pattern)
        entropy = math.log(math.pow(charset_len, pattern_len), 2)
        return round(entropy)
    
    def write_list(self, filepath, liste):
        with open(filepath, u'w') as f:
            for entry in list: f.write(entry)


parser = argparse.ArgumentParser(description=u"Génération de mots de passe aléatoires.",
                                 formatter_class=RawTextHelpFormatter)
parser.add_argument(u'pattern', help=u"format du mot de passe: \n \
                                    %s pour les CONSONNES \n \
                                    %s pour les consonnes \n \
                                    %s pour les VOYELLES \n \
                                    %s pour les voyelles \n \
                                    %s pour les LETTRES \n \
                                    %s pour les lettres \n \
                                    %s pour les nombres \n \
                                    %s pour la ponctuation étendue \n \
                                    %s pour la ponctuation"
                                    % (CONSO_MAJ, CONSO_MIN, VOWEL_MAJ, VOWEL_MIN,
                                       LETTER_MAJ, LETTER_MIN, NUMBER, PONCTION, PONCTION_SMA))
parser.add_argument(u'-n', u'--number', type=int, default=1, help=u"nombre de mdp à générer")
parser.add_argument(u'-o', u'--output', type=argparse.FileType('w'), help=u"fichier de sortie")
parser.add_argument(u'-e', u'--entropy', action=u"store_true", help=u"affiche l'entropie des mdp générés en bits")

args = parser.parse_args() #[u'Cvcvnnnn', u'-en', u'35', u'-o', u'pass.txt']

rand_p = RandomPassword()

# ENTROPY
if(args.entropy):
    print(u"L'entropie est de %s bits." % rand_p.get_entropy(args.pattern))

# LIST PASSWORDS
passwords = rand_p.get_passwords(args.pattern, iterations=args.number)
print(u"\nListe des mots de passe:")
for entry in passwords: print(u" - %s" % entry)

# WRITE PASSWORDS
if(args.output):
    with args.output as f:
        for entry in passwords: f.write(u'%s\n' % entry)
