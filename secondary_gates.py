# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 11:14:08 2021

@author: Vishwesh
"""
import numpy as np
import matplotlib.pyplot as plt
from basic_gates import AND, OR, NOT, NAND, NOR,XNOR,XOR, binary_check,length_check
#%%
def AND_AND (A,B,C,D):
    """realisation of AND-AND gate
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]

    Returns
    -------
    x : list[]
        intermediate output of A AND B
    y : list[]
        intermediate output of C AND D
    z : list[]
        Final output of x AND y

    """
    z=[]
    x=AND(A,B)
    y=AND(C,D)
    z=AND(x,y)
    return x,y,z
#%%
def AND_OR (A,B,C,D):
    """realisation of AND-OR gate
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]

    Returns
    -------
    x : list[]
        intermediate output of A AND B
    y : list[]
        intermediate output of C AND D
    z : list[]
        Final output of x OR y

    """
    z=[]
    x=AND(A,B)
    y=AND(C,D)
    z=OR(x,y)
    return x,y,z
#%%
def AND_NAND (A,B,C,D):
    """realisation of AND-NAND gate
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]

    Returns
    -------
    x : list[]
        intermediate output of A AND B
    y : list[]
        intermediate output of C AND D
    z : list[]
        Final output of x AND y

    """
    z=[]
    x=AND(A,B)
    y=AND(C,D)
    z=NAND(x,y)
    return x,y,z
#%%
def AND_NOR (A,B,C,D):
    """realisation of AND-NOR gate
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]

    Returns
    -------
    x : list[]
        intermediate output of A AND B
    y : list[]
        intermediate output of C AND D
    z : list[]
        Final output of x NOR y

    """
    z=[]
    x=AND(A,B)
    y=AND(C,D)
    z=NOR(x,y)
    return x,y,z
#%%
def OR_AND (A,B,C,D):
    """realisation of OR-AND gate
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]

    Returns
    -------
    x : list[]
        intermediate output of A OR B
    y : list[]
        intermediate output of C OR D
    z : list[]
        Final output of x AND y

    """
    z=[]
    x=OR(A,B)
    y=OR(C,D)
    z=AND(x,y)
    return x,y,z
#%%
def OR_OR (A,B,C,D):
    """realisation of OR-OR gate
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]

    Returns
    -------
    x : list[]
        intermediate output of A OR B
    y : list[]
        intermediate output of C OR D
    z : list[]
        Final output of x OR y

    """
    z=[]
    x=OR(A,B)
    y=OR(C,D)
    z=OR(x,y)
    return x,y,z
#%%
def OR_NAND (A,B,C,D):
    """realisation of OR-NAND gate
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]

    Returns
    -------
    x : list[]
        intermediate output of A OR B
    y : list[]
        intermediate output of C OR D
    z : list[]
        Final output of x NAND y

    """
    z=[]
    x=OR(A,B)
    y=OR(C,D)
    z=NAND(x,y)
    return x,y,z
#%%
def OR_NOR (A,B,C,D):
    """realisation of OR-NOR gate
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]

    Returns
    -------
    x : list[]
        intermediate output of A OR B
    y : list[]
        intermediate output of C OR D
    z : list[]
        Final output of x NOR y

    """
    z=[]
    x=OR(A,B)
    y=OR(C,D)
    z=NOR(x,y)
    return x,y,z
#%%
def NAND_AND (A,B,C,D):
    """realisation of NAND-AND gate
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]

    Returns
    -------
    x : list[]
        intermediate output of A NAND B
    y : list[]
        intermediate output of C NAND D
    z : list[]
        Final output of x AND y

    """
    z=[]
    x=NAND(A,B)
    y=NAND(C,D)
    z=AND(x,y)
    return x,y,z
#%%
def NAND_OR (A,B,C,D):
    """realisation of NAND-OR gate
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]

    Returns
    -------
    x : list[]
        intermediate output of A NAND B
    y : list[]
        intermediate output of C NAND D
    z : list[]
        Final output of x OR y

    """
    z=[]
    x=NAND(A,B)
    y=NAND(C,D)
    z=OR(x,y)
    return x,y,z
#%%
def NAND_NAND (A,B,C,D):
    """realisation of NAND-NAND gate
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]

    Returns
    -------
    x : list[]
        intermediate output of A NAND B
    y : list[]
        intermediate output of C NAND D
    z : list[]
        Final output of x NAND y

    """
    z=[]
    x=NAND(A,B)
    y=NAND(C,D)
    z=NAND(x,y)
    return x,y,z
#%%
def NAND_NOR (A,B,C,D):
    """realisation of NAND-NOR gate
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]

    Returns
    -------
    x : list[]
        intermediate output of A NAND B
    y : list[]
        intermediate output of C NAND D
    z : list[]
        Final output of x NOR y

    """
    z=[]
    x=NAND(A,B)
    y=NAND(C,D)
    z=NOR(x,y)
    return x,y,z
#%%
def NOR_AND (A,B,C,D):
    """realisation of NOR-AND gate
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]

    Returns
    -------
    x : list[]
        intermediate output of A NOR B
    y : list[]
        intermediate output of C NOR D
    z : list[]
        Final output of x AND y

    """
    z=[]
    x=NOR(A,B)
    y=NOR(C,D)
    z=AND(x,y)
    return x,y,z
#%%
def NOR_OR (A,B,C,D):
    """realisation of NOR-OR gate
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]

    Returns
    -------
    x : list[]
        intermediate output of A NOR B
    y : list[]
        intermediate output of C NOR D
    z : list[]
        Final output of x OR y

    """
    z=[]
    x=NOR(A,B)
    y=NOR(C,D)
    z=OR(x,y)
    return x,y,z
#%%
def NOR_NAND (A,B,C,D):
    """realisation of NOR-NAND gate
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]

    Returns
    -------
    x : list[]
        intermediate output of A NOR B
    y : list[]
        intermediate output of C NOR D
    z : list[]
        Final output of x NAND y

    """
    z=[]
    x=NOR(A,B)
    y=NOR(C,D)
    z=NAND(x,y)
    return x,y,z
#%%
def NOR_NOR (A,B,C,D):
    """realisation of NOR-NOR gate
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]

    Returns
    -------
    x : list[]
        intermediate output of A NOR B
    y : list[]
        intermediate output of C NOR D
    z : list[]
        Final output of x NOR y

    """
    z=[]
    x=NOR(A,B)
    y=NOR(C,D)
    z=NOR(x,y)
    return x,y,z
#%%















