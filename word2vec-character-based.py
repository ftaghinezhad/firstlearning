
import numpy as np

#------------------------------------------------------------------Initializing
alphabet_num = 26
max_lenght_of_words = 10

weight_input_ch = np.zeros((max_lenght_of_words,alphabet_num))
character_code = np.ones((alphabet_num))
weight_f=np.zeros((max_lenght_of_words))
word = np.zeros((max_lenght_of_words,alphabet_num))

#----------------------------------------------------Reading and Preparing Data
