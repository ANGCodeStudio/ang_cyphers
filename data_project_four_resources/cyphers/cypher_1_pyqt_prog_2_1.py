# -*- coding: utf-8 -*-
"""
This module contains a few simple cyphers. 
Created on Tue Jun 22 20:13:09 2021
@author: ANG
"""
import string
import numpy as np
from .ang_tools import reshape_calc

''' 
One of my favorite things to do is make cyphers. Are they anything like what you 
see in AES encryption? No. These cyphers are not secure. But, it is a fun 
exersize in data type methods. 

One of my favorite things to read about is the history of cyphers too. 
One of the earliest known cyphers was the Ceasar Cypher. Julius Ceasar 
was known to send encoded messages he wanted to keep secret by 
shifting the letters of the alphabet. The traditional Ceasar Cypher uses a shift 
value of three. 
''' 

def c_c_3_1(some_string, enc): 
    '''
    Simple Ceasar cypher.
    Rotates backward 6. 
    This function accepts only lower case ascii characters. 
    Pass a string to cypher it; enc = True 
    Pass a cyphered list to decypher it; enc = False 
    ''' 
    char_set = [i for i in string.ascii_lowercase] #creates a list of all ascii lowcase
    char_keys = [i for i in range(0,100)]          #creates a list of int 0-100
    char_dict = dict(zip(char_keys, char_set))     #creates a dict where: {char_keys: "char_set"}
    dk_c = [] #this list holds the key values for the some_string to the function
    sv_1 = [] #
    #y = totalNumItems; shift = ShiftSize ; i=intIndexOfItem ; z=MaxPossibleIndexShiftFrom(0-1)
    x = ''               #the finished encoded or decoded string 
    tot = len(char_dict) #The size of the dictionary 
    shift = 6            #the number of spaces to shift the string
    z1 = shift - 1   #z1 is neccesary because the index of the string always starts at 0 
    #CHARACTER SET ENUMERATION CONVERSION 
    for si in some_string:                #for string items in the string passed
        for dk, dv in char_dict.items():  #for all the dict keys and values in char_dict
            if si == dv:                  #if the string item equals the char_dict value
                dk_c.append(dk)           #dk_c will append the key value
    if enc == True: #starts encoding if encoding is True
        #iterate through every indexed item in dk_c and subtract shift  
        #or y = totalNumItems; x = ShiftSize ; i=intIndexOfItem ; z=MaxPossibleIndexShiftFromZero 
        #       [abs(abs(i - y)-x) if i < x else i - x for items in dk_c] 
        dk_c2 = [abs(abs(-i - tot)-shift) if i <= z1 else i - shift for i in dk_c]
    else: 
        #dictKey_cypher2 = [item - RotationSize if item lessThan or equalTo RotationSize else absoluteVal(-item - totItems)-stepSize) for items in dk_c]
        #or y = maxIndexNum; x = ShiftSize ; i=intIndexOfItem ; 
        #       [abs(abs(i - y)-x) if i >= y-x else i + x for i in dk_c]
        dk_c2 = [abs(abs(i - tot)-shift) if i >= tot-shift else i + shift for i in dk_c] 
    for si2 in dk_c2:                     #for every item in the cypher list of keys 
        for dk, dv in char_dict.items():  #for all the dict keys and values in char_dict
            if si2 == dk:                 #if the string item equals the char_dict value 
                sv_1.append(dv)           
    for i3 in sv_1:
        x += i3
    else: 
        pass 
    return x

'''
You can make these even more complex by using all the printable string data. 
Which are the following:
0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c

So, instead of using just lowercase letters you have a lot more data to encode. 
For the Ceasar cypher it is done pretty much the same way you just start with 
a dictionary that is larger. 
''' 
def c_c_3_2(some_string, enc): 
    ''' 
    Simple Ceasar cypher.
    Rotates backward 6. 
    This function accepts any printable characters. 
    Pass a string to cypher it; enc = True 
    Pass a cyphered list to decypher it; enc = False 
    ''' 
    char_set = [i for i in string.printable] #creates a list of all ascii lowcase
    char_keys = [i for i in range(0,100)]          #creates a list of int 0-100
    char_dict = dict(zip(char_keys, char_set))     #creates a dict where: {char_keys: "char_set"}
    dk_c = [] #this list holds the key values for the some_string to the function
    sv_1 = [] #
    #y = totalNumItems; shift = ShiftSize ; i=intIndexOfItem ; z=MaxPossibleIndexShiftFrom(0-1)
    x = ''               #the finished encoded or decoded string 
    tot = len(char_dict) #The size of the dictionary 
    shift = 6            #the number of spaces to shift the string
    z1 = shift - 1       #z1 is neccesary because the index of the string always starts at 0 
    #CHARACTER SET ENUMERATION CONVERSION 
    for si in some_string:                #for string items in the string passed
        for dk, dv in char_dict.items():  #for all the dict keys and values in char_dict
            if si == dv:                  #if the string item equals the char_dict value
                dk_c.append(dk)           #dk_c will append the key value
    if enc == True: #starts encoding if encoding is True
        #iterate through every indexed item in dk_c and subtract shift  
        #or y = totalNumItems; x = ShiftSize ; i=intIndexOfItem ; z=MaxPossibleIndexShiftFromZero 
        #       [abs(abs(i - y)-x) if i < x else i - x for items in dk_c] 
        dk_c2 = [abs(abs(-i - tot)-shift) if i <= z1 else i - shift for i in dk_c]
    else: 
        #dictKey_cypher2 = [item - RotationSize if item lessThan or equalTo RotationSize else absoluteVal(-item - totItems)-stepSize) for items in dk_c]
        #or y = maxIndexNum; x = ShiftSize ; i=intIndexOfItem ; 
        #       [abs(abs(i - y)-x) if i >= y-x else i + x for i in dk_c]
        dk_c2 = [abs(abs(i - tot)-shift) if i >= tot-shift else i + shift for i in dk_c] 
    for si2 in dk_c2:                     #for every item in the cypher list of keys 
        for dk, dv in char_dict.items():  #for all the dict keys and values in char_dict
            if si2 == dk:                 #if the string item equals the char_dict value 
                sv_1.append(dv)           #append it to sv_1
    for i3 in sv_1:   #for every string in sv_1 (a list)
        x += i3       #append it to x 
    else: 
        pass 
    return x   #return the string 

'''
Although, substitution cyphers are easy to crack by frequency analysis or guessing 
the shift value with a brute force attack—in the case where someone reasonably 
suspects a substitution cypher is being used. 

Brute forcer:
Say we know only that someone used a Ceasar Cypher, only used lowercase letters 
and the index of the letters they used were in order abcd... | 0123...

We do not know the dirction they rotated the letters or by how many letters they 
rotated the substitution. 
'''
def brute_force_0(some_enc_string): 
    '''
    This function will output all possible decodings given a Ceasar Cypher 
    that uses only lower case letters. 
    '''
    char_set = [i for i in string.ascii_lowercase] 
    char_keys = [i for i in range(0,100)] 
    char_dict = dict(zip(char_keys, char_set)) 
    dk_c = [] #
    g_s_s = [] 
    shift = 0 
    tot = 26 
    #CHARACTER SET ENUMERATION CONVERSION
    for si in some_enc_string:            #for string items in the string passed
        for dk, dv in char_dict.items():  #for all the dict keys and values in char_dict
            if si == dv:                  #if the string item equals the char_dict value
                dk_c.append(dk)           #dk_c will append the key value
    for i in range(26):
        sv_1 = []
        x_s = ''
        #or y = totalNumItems; x = ShiftSize ; i=intIndexOfItem ; 
        for i in dk_c:
            dk_c2 = [abs(abs(i - tot)-shift) if i >= tot-shift else i + shift for i in dk_c]
            
            for si2 in dk_c2: #for every item in the cypher list of keys
                for dk, dv in char_dict.items():  #for all the dict keys and values in char_dict
                    if si2 == dk:                 #if the string item equals the char_dict value
                        sv_1.append(dv) 
            for i3 in sv_1:
                x_s += i3
            else: 
                pass 
            if len(x_s) == len(some_enc_string): 
                g_s_s.append(x_s) 
        shift += 1 
    return g_s_s 

'''
You can tweak the brute forcer to crack this too. 
'''
def brute_force_1(some_enc_string): 
    char_set = [i for i in string.printable] #all printable strings
    char_keys = [i for i in range(0,100)] 
    char_dict = dict(zip(char_keys, char_set)) 
    dk_c = []  
    
    g_s_s = [] 
    shift = 0 
    y = 100
    
    #CHARACTER SET ENUMERATION CONVERSION
    for si in some_enc_string:            #for string items in the string passed
        for dk, dv in char_dict.items():  #for all the dict keys and values in char_dict
            if si == dv:                  #if the string item equals the char_dict value
                dk_c.append(dk)          #dk_c will append the key value
    for i in range(100):
        sv_1 = []
        x_s = ''
        #or y = totalNumItems; x = ShiftSize ; i=intIndexOfItem ; 
        for i in dk_c:
            dk_c2 = [abs(abs(i - y)-shift) if i >= y-shift else i + shift for i in dk_c]
            
            for si2 in dk_c2: #for every item in the cypher list of keys
                for dk, dv in char_dict.items():  #for all the dict keys and values in char_dict
                    if si2 == dk:                  #if the string item equals the char_dict value
                        sv_1.append(dv) 
            for i3 in sv_1:
                x_s += i3
            else: 
                pass 
            if len(x_s) == len(some_enc_string): 
                g_s_s.append(x_s) 
        shift += 1
    return g_s_s

''' 
You can add more difficulty by adding extra steps. So, a_c_1,  a_c_2, and  a_c_3 
are all substitution cyphers. Where a_c_1 and a_c_2 return the index of the letters, in 
the char_dict, as a list with some applied math operation and a_c_3 returns an array. 
In this case it is very simple. 
''' 
def a_c_1(vals, enc): 
    ''' 
    ex: a_c_1('SomeStringToEncode', True)
    Pass a string to cypher it; enc = True 
    Pass a cyphered list to decypher it; enc = False
    '''
    char_set = [i for i in string.printable]
    char_keys = [i for i in range(1,101)]
    char_dict = dict(zip(char_keys, char_set))
    x = ''
    dk_c = []
    if enc == True:
        #CHARACTER SET ENUMERATION CONVERSION 
        for si in vals:                       #for string items in the string passed
            for dk, dv in char_dict.items():  #for all the dict keys and values in char_dict
                if si == dv:                  #if the string item equals the char_dict value
                    dk_c.append(dk)           #dk_c will append the key value
                    
        #iterate through every key and add 3 
        for idx, i in enumerate(dk_c):
                dk_c[idx] = int(dk_c[idx]+3)
        return dk_c
    else: 
        #iterate through every key and subract 3 
        for idx, i in enumerate(vals):
                vals[idx] = int(vals[idx]-3)
        for i in vals:
            x += char_dict[i]
        return x


def a_c_2(vals, enc): 
    ''' 
    ex: a_c_2('SomeStringToEncode', True)
    Pass a string to cypher it; enc = True 
    Pass a cyphered list to decypher it; enc = False
    '''
    char_set = [i for i in string.printable]
    char_keys = [i for i in range(1,101)]
    char_dict = dict(zip(char_keys, char_set))
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
                dk_c[idx] = int(dk_c[idx]+3)
            else: 
                dk_c[idx] -= 5
        return dk_c
    else: 
        #iterate through every even key and subract 3 else add 5
        for idx, i in enumerate(vals):
            if idx % 2 == 1: 
                vals[idx] = int(vals[idx]-3)
            else: 
                vals[idx] += 5
        for i in vals:
            print(char_dict[i], end='')
        return 


def a_c_3(vals, enc): 
    ''' 
    ex: a_c_3('SomeStringToEncode', True)
    Pass a string to cypher it; enc = True 
    Pass a cyphered list to decypher it; enc = False
    '''
    char_set = [i for i in string.printable]
    char_keys = [i for i in range(1,101)]
    char_dict = dict(zip(char_keys, char_set))
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
                dk_c[idx] = int(dk_c[idx]+3)
            else: 
                dk_c[idx] -= 5
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
                vals[idx] = int(vals[idx]-3)
            else: 
                vals[idx] += 5
        for i in vals:
            print(char_dict[i], end='')
        return 

