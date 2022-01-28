# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 15:41:59 2022

@author: ANG
"""
import string
import numpy as np
from .ang_tools import reshape_calc 
import random

def a_d_1(vals, pwd, enc): 
    ''' 
    ex: a_c_1('Some string to encode', pwd='Some_password', enc=True)
    Pass a string to cypher it; enc = True 
    Pass a cyphered list to decypher it; enc = False
    '''
    char_set = [i for i in string.printable]
    char_keys = [i for i in range(1,101)]
    char_dict = dict(zip(char_keys, char_set))
    pwd = hash(pwd)
    if enc == True:
        #CHARACTER SET ENUMERATION CONVERSION 
        dk_c = []
        for si in vals:                       #for string items in the string passed
            for dk, dv in char_dict.items():  #for all the dict keys and values in char_dict
                if si == dv:                  #if the string item equals the char_dict value
                    dk_c.append(dk)           #dk_c will append the key value
                    
        #iterate through every even indexed item and add 3 else subtract 5 
        for idx, i in enumerate(dk_c): 
            if idx % 2 == 1: 
                dk_c[idx] = int(dk_c[idx]+3) + pwd
            else: 
                dk_c[idx] -= 5 + pwd
        #Calculates the possible reshapes given the len of the string 
        new_shape = reshape_calc(len(dk_c), 3)  
        #Converts the list into an array & reshapes it with the last item in new_shape
        dk_c = np.array(dk_c).reshape(new_shape[-1])
        return dk_c
    else: 
        #Convert the array back to a list
        vals = list(vals.reshape(vals.size,))
        #iterate through every even key and subract 3 else add 5 
        for idx, i in enumerate(vals):
            if idx % 2 == 1: 
                vals[idx] = int(vals[idx]-3) - pwd
            else: 
                vals[idx] += 5 + pwd
        for i in vals:
            print(char_dict[i], end='')
        return 

def sim_aes_0(vals, key, enc): 
    ''' 
    vals = 'some string to encode'
    key = 'someString16charactersLong'
    
    enc = True
    Takes the key and applies a key expansion to generate 9 more unique keys 
    Takes a plain text str and converts it to a bytearray() -> converts it to a 
    3d array ->  pads with random data if it is not divisible by 16 -> substitutes 
    data depending on axes location -> mixes rows/cols -> applies a new key to 
    the array depending on round
    
    enc = False
    Does the reverse of enc. 
    ''' 
    #convert the key to an array 
    #HERE 
    key = [i for i in bytearray(key, 'ascii')]
    key = np.array(key).reshape(-1,4,4)

    def expand_key(key):
        #expand the key here 
        #roll the key words 
        key_r1 = [i for i in np.roll(key[0], 1, 1)]
        key_r1 = np.vstack(key_r1) 
        key_r1 = key_r1.ravel()
        #substitute vals HERE (arbitrary substitution)
        key_r1 = np.array([i + 16 if (i % 2 == 0) else i for i in key_r1]).reshape(-1,4,4)
        #xor rows with xor word 
        xor_w = np.array([13, 0, 0, 0])
        key_r1 = np.array([v^xor_w for v in key_r1])
        return key_r1 
    key_0 = expand_key(key) 
    key_1 = expand_key(key_0)
    key_2 = expand_key(key_1)
    key_3 = expand_key(key_2)
    key_4 = expand_key(key_3)
    key_5 = expand_key(key_4)
    key_6 = expand_key(key_5)
    key_7 = expand_key(key_6)
    key_8 = expand_key(key_7)
    key_9 = expand_key(key_8)
    keys_dict = {0:key_0, 1:key_1, 2:key_2, 
                 3:key_3, 4:key_4, 5:key_5, 
                 6:key_6, 7:key_7, 8:key_8, 
                 9:key_9}
    #substitution table parts
    string_lst = [i for i in bytearray(string.printable, 'ascii')]
    if enc == True: 
        #CYPHER THE ARRAY
        #bit encoding for string data (arg vals)
        #sequence; str -> bytearray ascii (strings) -> int -> hex
        vals_ph = [i for i in bytearray(vals, 'ascii')] #STEP 1 STRING TO BYTEARRAY
        vals_arr = np.array(vals_ph) 
        #the size of vals_arr has to be a multiple of 16 
        if vals_arr.size % 16 == 0: 
            vals_arr = vals_arr.reshape(-1, 4, 4) 
        else: 
            while vals_arr.size % 16 != 0: 
                #apply random pad at the end if the array size is not divisible by 16
                vals_arr = np.append(vals_arr, random.choice(string_lst)) 
            vals_arr = vals_arr.reshape(-1, 4, 4) 
        #convert string to int 
        vals_arr = vals_arr.astype(int)  #BYTEARRAY TO INT
        #Apply ROUNDS HERE 
        def round_nth(vals_arr): 
            for i in range(10):
                #SUB BYTES 
                for i2 in range(vals_arr.shape[0]):
                    if i2 % 2 == 1:
                        vals_arr[i2] += 2
                    else: 
                        vals_arr[i2] -= 2
                #MIX ROWS / MIX COLS 
                vals_arr = np.roll(vals_arr, 1, 0) 
                vals_arr = np.roll(vals_arr, 1, 1) #shift rows for each axis0 down 1; last row becomes first row, and last row becomes first row
                vals_arr = np.roll(vals_arr, 1, 2) #shift axes 2 up one for each item in axes0            
                #ADD Nth ROUND KEY 
                vals_arr = vals_arr^keys_dict[i]
            return vals_arr
        vals_arr = round_nth(vals_arr)
        #flatten cyphered array 
        vals_arr = vals_arr.flatten()
        output = ' '.join(map(str, vals_arr)).split()
        output = [int(i) for i in output]
        #output = bytearray(list(output)).decode('ascii')
        return output
    else: 
        #DECYPHER THE ARRAY
        #bit encoding for string data (arg vals)
        #sequence; str -> bytearray ascii (strings) -> int 
        vals_arr = np.array(vals) 
        vals_arr = vals_arr.reshape(-1, 4, 4) 
        #convert string to int 
        vals_arr = vals_arr.astype(int)  #BYTEARRAY TO INT
        #Apply ROUNDS HERE 
        def round_nth(vals_arr): 
            for i in range(9, -1, -1):
                #REVERSE Nth ROUND KEY 
                vals_arr = vals_arr^keys_dict[i]  
                #MIX ROWS / MIX COLS 
                vals_arr = np.roll(vals_arr, -1, 0) 
                vals_arr = np.roll(vals_arr, -1, 1) #shift rows for each axis0 down 1; last row becomes first row, and last row becomes first row
                vals_arr = np.roll(vals_arr, -1, 2) #shift axes 2 up one for each item in axes0  
                #SUB BYTES 
                for i in range(vals_arr.shape[0]):
                    if i % 2 == 1:
                        vals_arr[i] -= 2
                    else: 
                        vals_arr[i] += 2
            return vals_arr 
        
        vals_arr = round_nth(vals_arr)
        #flatten cyphered array 
        vals_arr = vals_arr.flatten()
        output = ' '.join(map(str, vals_arr)).split()
        output = [int(i) for i in output]
        output = bytearray(list(output)).decode('ascii')
        return output
