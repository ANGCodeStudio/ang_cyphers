# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 15:41:59 2022

@author: ANG
"""
import numpy as np
import glob 
import inspect 
np.set_printoptions( threshold=20, edgeitems=10, linewidth=119,)

'''
When importing explicit is better than implicit. So, here I import cypher_1_pyqt_prog_2_1
from cyphers. 
'''
from cyphers import cypher_1_pyqt_prog_2_1 as cypher_m #imports the file cypher_1_pyqt_prog_2_1.py from the dir cyphers
from cyphers import adv_arr_cyphers as advc

'''
Really good example of exploring the directory. 
'''
def show_direct():
    print('Current local scope:', *dir(), '\n', sep='\n')
    print('Current working directory:', *glob.glob('./**'), '\n', sep='\n')
    print('Sub Folder Content for Cyphers:', *glob.glob('./cyphers/**'), '\n', sep='\n') 
    print('All functions in imported modules:', 
          'cypher_m',
          *inspect.getmembers(cypher_m, inspect.isfunction),
          'advc',
          *inspect.getmembers(advc, inspect.isfunction),
          sep='\n')
    return
