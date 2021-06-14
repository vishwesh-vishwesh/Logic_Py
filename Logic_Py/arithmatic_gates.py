# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 11:01:59 2021

@author: Vishwesh
"""
from basic_gates import AND, OR, NOT, NAND, NOR,XNOR,XOR

#%%
def half_adder(A,B):
    """Half Adder realisation

    Parameters
    ----------
    A : list[]
    B : list[]

    Returns
    -------
    S : list[]
        Sum of two inputs
    C : list[]
        Carry of two inputs 

    """
    S = XOR (A,B)
    C = AND(A,B)
    return S,C
#%%
def full_adder(A,B,Cin):
    """Full Adder realisation - 3 bit Binary input

    Parameters
    ----------
    A : list[]
    B : list[]
    Cin : list[]
        Carry input bit

    Returns
    -------
    S : list[]
        sum of three inputs
    Cout : list[]
        carry of three inputs

    """
    S_1,C_1 = half_adder(A,B)
    S,C_2 = half_adder(Cin,S_1)
    Cout = OR(C_2,C_1)
    return S,Cout

#%%





















