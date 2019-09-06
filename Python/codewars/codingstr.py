#!/usr/bin/env python3

import string
from codecs import encode as _dont_use_this_
import re

def rot13(message):
    letter = message.split(' ')
    for i in range(len(letter)):
        if letter[i] == 'h':
            letter[i] = 'u'
    return letter

print(rot13('hello'))
    