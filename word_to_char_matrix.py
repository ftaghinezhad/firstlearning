# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 16:35:06 2023

@author: givi
"""
import numpy as np

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
max_lenght_of_words=10
alphabet_num=26

# word: String, max_length_of-words: number, alphabet_num: number, alphabet: list of alphabet
def word_to_input(word, max_lenght_of_words, alphabet_num, alphabet):
    word_matrix = np.zeros((max_lenght_of_words, alphabet_num))
    w = list(word)
    
    i=0
    for ch in w:
        #print(ch)
        word_matrix[i][alphabet.index(ch)]=1
        i = i+1
    
    return word_matrix
#-------ENd of function
    