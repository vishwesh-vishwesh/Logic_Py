# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 10:24:51 2021

@author: Vishwesh
"""

from basic_gates import AND, OR, NOT, NAND, NOR,XNOR,XOR
from secondary_gates import  AND_OR
#%%
def Binary2Gray(A,B,C,D):
    """4 bit Binary to Gray converter
    
    Parameters - input Binary code
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]

    Returns - outputs the Gray code
    -------
    w : list[]
    x : list[]
    y : list[]
    z : list[]

    """
    w = A
    x = XOR (A,B)
    y = XOR (B,C)
    z = XOR (C,D)
    return w,x,y,z
#%%
def Gray2Binary(A,B,C,D):
    """4 bit Gray to Binary converter
    
    Parameters - input gray code
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]

    Returns - outputs the binary code
    -------
    w : list[]
    x : list[]
    y : list[]
    z : list[]

    """
    w = A
    x = XOR (A,B)
    y = XOR (x,C)
    z = XOR (y,D)
    return w,x,y,z
#%% 
def EParity_gen(A,B,C):
    """3 bit Even Parity generator for 3 bit Binary input
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]

    Returns
    -------
    parity : list[]
        generated even parity bit

    """
    z = XOR (A,B)
    parity = XOR (z,C)
    return parity
#%%

def OParity_gen(A,B,C):
    """3 bit Even Parity generator for 3 bit Binary input
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]

    Returns
    -------
    parity : list[]
        generated even parity bit

    """
    z = XOR (A,B)
    parity = XNOR (z,C)
    return parity

#%%

def EParity_check(A,B,C,P):
    """Even Parity Checker for 3 bit binary input with a parity bit P (4-bit input in total)
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    P : list[]
        Even parity bit as 4th input
        (Condition : Program outputs a value even if the P value is not an Even parity bit,
        it is prerogative of user use the correct P value for input)

    Returns
    -------
    E : list[]
        outputs an Even parity check bit, E[i] will be 1 if the input at i has odd number of 1s.

    """
    x = XOR (A,B)
    y = XOR (C,P)
    E = XOR (x,y)
    return E

#%%

def OParity_check(A,B,C,P):
    """Odd Parity Checker for 3 bit binary input with a parity bit P (4-bit input in total)
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    P : list[]
        Odd parity bit as 4th input
        (Condition : Program outputs a value even if the P value is not an appropriate Odd parity bit,
        it is prerogative of user to use the correct P value for input)

    Returns - Odd parity check bit
    -------
    O : list[]
        outputs an Odd parity check bit, O[i] will be 1 if the input at i has even number of 1s.
    """    
    x = XOR (A,B)
    y = XOR (C,P)
    O = XNOR (x,y)
    return O
#%%    

def BCD2Excess3(A,B,C,D):
    '''BCD to excess3 converter
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]

    Returns
    -------
    w : list[]
    x : list[]
    y : list[]
    z : list[]

    '''
    z   = NOT(D)
    y_1 = AND (D,C)
    y_2 = OR (D,C)
    y_3 = NOT(y_2)
    y   = OR (y_1,y_3)
    x_1 = NOT (B)
    x   = AND_OR (y_3,B,y_2,x_1)
    w_1 = AND (y_2,B)
    w   = OR (w_1,A)
    return w,x[2],y,z
#%%

def Excess32BCD(A,B,C,D):
    '''Excess3 to BCD converter

    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]

    Returns
    -------
    w : list[]
    x : list[]
    y : list[]
    z : list[]

    '''
    w1 = AND (C,D)
    w = (AND_OR(A,w1,A,B))[2]
    x1 = (AND_OR(NOT(B),NOT(C),NOT(B),NOT(D)))[2]
    x2 = (AND(AND(B,C),D))
    x = OR(x1,x2)
    y = AND_OR(NOT(C),D,C,NOT(D))[2]
    z = NOT(D)
    return w,x,y,z

#%%
    

