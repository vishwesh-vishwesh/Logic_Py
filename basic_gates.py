# -*- coding: utf-8 -*-

"""
Created on Sun Jun  6 15:21:25 2021

@author: Vishwesh
"""
import numpy as np
import scipy
import matplotlib.pyplot as plt
#%%
#d = (int,input("number:"))
     
#%% OR gate

def OR (A,B):
    result=[]
    for i in range(len(A)):
        
        if A[i] == 1 or B[i] == 1:
            result.append(1)
        else:
            result.append(0)
    return result

#%% AND gate

def AND (A,B):
    result=[]
    for i in range(len(A)):
        
        if A[i] == 1 and B[i] == 1:
            result.append(1)
        else:
            result.append(0)
    return result

#%% not
def NOT (A):
    result=[]
    for i in range(len(A)):
        
        if A[i] == 1:
            result.append(0)
        else:
            result.append(1)
    return result
                
#%% nand
def NAND (A,B):
    result=[]
    for i in range(len(A)):
        
        if A[i] == 1 and B[i] == 1:
            result.append(0)
        else:
            result.append(1)
    return result

#%% nor

def NOR (A,B):
    result=[]
    for i in range(len(A)):
        
        if A[i] == 1 or B[i] == 1:
            result.append(0)
        else:
            result.append(1)
    return result

#%% XNOR

def XNOR (A,B):
    result=[]
    for i in range(len(A)):
        
        if A[i] == 1 and B[i] == 1:
            result.append(1)
        elif A[i] == 0 and B[i] == 0:
            result.append(1)    
        else:
            result.append(0)
    return result

#%% XOR
def XOR (A,B):
    result=[]
    for i in range(len(A)):
        
        if A[i] == 1 and B[i] == 1:
            result.append(0)
        elif A[i] == 0 and B[i] == 0:
            result.append(0)    
        else:
            result.append(1)
    return result

#%%
'''
x =[0, 1, 1, 1, 1]
y = [0, 1, 1, 1, 1]
z = [0, 1, 1, 1, 0]

aans = AND (AND (x,y), AND (x,z))
#%%
aans2= NOT(x)
'''


