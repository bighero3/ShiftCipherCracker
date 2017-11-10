# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 09:34:03 2017

@author: Abhinav
"""

def shift(string,shift):
    newstring=""
    for x in string:
        newstring+=chr(ord(x)+shift)
    return newstring

def unshift(string):
    from nltk.corpus import words
    for x in range(1,27,1):
        attempt= shift(string, -x)
        attempt=attempt.split(" ")
        for z in attempt:
            if z in words.words():
                print(attempt)
                print(x)