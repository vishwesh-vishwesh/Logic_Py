# -*- coding: utf-8 -*-

"""
Created on Sun Jun  6 15:21:25 2021

@author: Vishwesh
"""
import numpy as np
import scipy
import matplotlib.pyplot as plt

#%%

def binary_check(A,B):
    #args = list(args)
    #ans = []
    for i in range(len(A)):
        if A[i] == 1 or A[i] == 0:
            pass
            if B[i] == 1 or B[i] == 0:
                pass
            else:
                raise ValueError("input must be binary, 0 or 1 in second input index %d"%i)
        else:
            raise ValueError("input must be binary, 0 or  1 in first input index %d"%i)
            
#%%

def length_check(A,B):
    if len(A) == len(B):
        pass
    else:
        raise ValueError("Length of both inputs must be same")
        
#%%
def OR (A,B):
    """realisation of AND gate
    
    Parameters
    ----------
    A : list[]
        0 or 1
    B : list[]
        0 or 1

    Returns
    -------
    result : list[]

    """
    binary_check(A,B)
    length_check(A, B)
    result=[]
    for i in range(len(A)):
        
        if A[i] == 1 or B[i] == 1:
            result.append(1)
        else:
            result.append(0)
        
    return result

#%%
def AND (A,B):
    """realisation of AND gate

    Parameters
    ----------
    A : list[]
        0 or 1
    B : list[]
        0 or 1

    Returns
    -------
    result : list[]

    """
    binary_check(A,B)
    length_check(A, B)
    result=[]
    for i in range(len(A)):
        
        if A[i] == 1 and B[i] == 1:
            result.append(1)
        else:
            result.append(0)
    return result

#%%
def NOT (A):
    """realisation of NOT gate

    Parameters
    ----------
    A : list[]
        0 or 1

    Returns
    -------
    result : list[]

    """
    binary_check(A,A)
    result=[]
    for i in range(len(A)):
        
        if A[i] == 1:
            result.append(0)
        else:
            result.append(1)
    return result
                
#%%
def NAND (A,B):
    """realisation of NAND gate

    Parameters
    ----------
    A : list[]
        0 or 1
    B : list[]
        0 or 1

    Returns
    -------
    result : list[]
        
    """
    binary_check(A,B)
    length_check(A,B)
    result=[]
    for i in range(len(A)):
        
        if A[i] == 1 and B[i] == 1:
            result.append(0)
        else:
            result.append(1)
    return result

#%%
def NOR (A,B):
    """realisation of NOR gate

    Parameters
    ----------
    A : list[]
        0 or 1
    B : list[]
        0 or 1

    Returns
    -------
    result : list[]
        
    """
    binary_check(A,B)
    length_check(A,B)
    result=[]
    for i in range(len(A)):
        
        if A[i] == 1 or B[i] == 1:
            result.append(0)
        else:
            result.append(1)
    return result

#%% XNOR
def XNOR (A,B):
    """realisation of XNOR gate

    Parameters
    ----------
    A : list[]
        0 or 1
    B : list[]
        0 or 1

    Returns
    -------
    result : list[]
        
    """
    binary_check(A,B)
    length_check(A,B)
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
    """realisation of XOR gate

    Parameters
    ----------
    A : list[]
        0 or 1
    B : list[]
        0 or 1

    Returns
    -------
    result : list[]
        
    """
    binary_check(A,B)
    length_check(A,B)
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

