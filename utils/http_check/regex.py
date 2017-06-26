# -*- coding: utf-8 -*-
# tools, 8 juin 2017

import re

if __name__ == '__main__':
    pass


#PAT_EMAIL = u'^(.+)@(.+)\.(.+)$'
#PAT_EMAIL = u'(.+)@(.+)\.(.+)'
#PAT_EMAIL = u'[^=\s@]@[^=\s@]\.[^=\s@]'
PAT_EMAIL = u'(\S+)@(\S+)\.(\S+)'


def check_regex(pattern, string):
    if re.search(pattern, string):
        return (True, string)
    return (False, string)

def check_regex_list(pattern, string_list):
    results = []
    for string in string_list:
        results.append(check_regex(pattern, string))
    return results


def count_regex(pattern, string):
    return (len(re.findall(pattern, string)), string)

def count_regex_list(pattern, string_list):
    results = []
    for string in string_list:
        results.append(count_regex(pattern, string))
    return results

