# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:13:09 2020

@author: Park
"""

from nltk.tokenize import word_tokenize
text = "I am actively lookin for Ph.D. students. and you are a Ph.D student."
print('=>', text); print()
print('=>', word_tokenize(text)); print()
from nltk.tag import pos_tag
x = word_tokenize(text)
print('=>', pos_tag(x))
