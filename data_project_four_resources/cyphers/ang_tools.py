# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 08:22:41 2021

@author: ANG
"""
import numpy as np
import itertools
import functools as f_tools
import warnings 
import random

def get_random_key(): 
    '''
    Function returns a random 128 bit key.
    '''
    hash = random.getrandbits(128)
    rand_key = hex(hash) 
    return rand_key

def reshape_calc(size, n_dims=2, **kwargs): 
    """
    reshape_calc(size = IntegerSizeOfAnArray, n_dims=NumberOfDimensions)
    Returns all posible shapes of a given array from array size factors defaulted to 2 dimensions.
    Any of the returned tuples can be re-ordered to fit array needs and will work in reshaping.     
    """
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    escape_1 = None
    if n_dims == 0:
        print('\nn_dims cannot equal zero.')
        return None
    f_lst = [] 
    shapes_actual = []
    shapes_actual_all = []
    escape_question = False
    is_prime = False
    n_dims_proxy = n_dims
    tup_list_lengths_proxy = False
    #####CREATE FACTOR LIST#####
    for i in range(1, size + 1): 
       if size % i == 0: 
           f_lst.append(i)
    #####IDENTIFY IF SIZE IS PRIME#####
    if len(f_lst) == 2: 
       #print(size, 'is a prime number.\n\nThe only possible shape is, one to any number of ones and itself--limited only by memory.')
       is_prime = True
    #####IDENTIFY IF SIZE FACTORS LIST IS LARGE#####
    if ((len(f_lst) > 45) & (n_dims > 6)): 
        print('This could take some time due to the size of the input.')
        escape_1 = input('Are you sure you want to continue [y] [n]: ')
        escape_question = True
    escape_options = ['y','n']
    if escape_1 not in escape_options and (escape_question == True):
        print("Input must be 'y' or 'n'")
    elif escape_1 == 'n':
        print('\nExecution Aborted')
        return None
    elif escape_1 == 'y': 
        print('This may take several minutes...')
    #####TURN FACTORS LIST TO ARRAY#####
    f_arr = np.asarray(f_lst, dtype=np.int64)
    #####TAKE THE DESIRED N_DIMS AND ALL THE PRODUCTS OF FACTORS THAT EQUAL THE SPECIFIED SIZE#####
    for i in range(n_dims):
        for i in np.arange(n_dims, n_dims+1, dtype=np.int64):
            combinations = itertools.combinations(f_arr, i)
            for i in combinations: 
                if f_tools.reduce(lambda x, y: x * y, i, 1) == size:
                    shapes_actual_all.append(i)
        n_dims -= 1
    #print("\nThe factors of",size,"are:", f_lst,'\n')
    #print('All possible shapes (which can be re-ordered) given the size and n_dims specified:\n')
    #####IF THE SIZE IS PRIME RETURN ONES AND SIZE#####
    #####ELIF THE SIZE IS NOT PRIME RETURN ALL SIZES PADDED BASED ON N_DIMS SPECIFIED#####
    if is_prime == True:
        new_shape = np.ones(n_dims_proxy-1, dtype=int)
        new_shape_lst = [i for i in new_shape]
        new_shape_lst.append(size)
        new_shape_lst = tuple(new_shape_lst)
        shapes_actual_all.append(new_shape_lst)
        for i in shapes_actual_all:
            if len(i) == n_dims_proxy:
                shapes_actual.append(i)
        return shapes_actual
    for i in shapes_actual_all:
        if len(i) == n_dims_proxy:
            shapes_actual.append(i)
            
    if len(shapes_actual) == 0:
        tup_list = [list(i) for i in shapes_actual_all]
        tup_list_lengths = [len(i) for i in tup_list]
        tup_list_lengths_proxy = True
    
    n_dims_padded = []
    if tup_list_lengths_proxy == True:
        if max(tup_list_lengths) < n_dims_proxy:
            for i in shapes_actual_all:
                new_shape = np.ones(n_dims_proxy-len(i), dtype=int)
                new_shape_lst = list(new_shape)
                new_shape_lst.extend(i)
                n_dims_padded.append(tuple(new_shape_lst))
            n_dims_padded_set = set(n_dims_padded)
            n_dims_padded_lst = list(n_dims_padded_set)
            return n_dims_padded_lst
                
    fin_return_tup_lst = []
    for i in shapes_actual_all: 
        if len(i) == n_dims_proxy:
            fin_return_tup_lst.append(i) 
    return fin_return_tup_lst

