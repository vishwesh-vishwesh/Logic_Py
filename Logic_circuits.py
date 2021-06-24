# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 01:51:14 2021

@author: Vishwesh
"""
from basic_gates import AND, OR, NOT, NAND, NOR,XNOR,XOR
from secondary_gates import AND_AND, OR_OR
import numpy as np
#%%

def Decoder2_4(A,B,E):
    '''2 to 4 bit Decoder

    Parameters
    ----------
    A : list[]
    B : list[]
    E : list[]
        Enable value

    Returns
    -------
    w : list[]
    x : list[]
    y : list[]
    z : list[]

    '''
    w = AND (E, AND(A,B))
    x = AND (E, AND(A,NOT(B)))
    y = AND (E, AND(NOT(A),B))
    z = AND (E, AND(NOT(A),NOT(A)))
    return w,x,y,z

#%%

def Decoder3_8(A,B,C):
    '''3 to 8 Decoder
    
    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]

    Returns
    -------
    x : list[4]
        list includes 4 more lists of 1 bit each making them first 4 bits of 8 bit output
    y : list[4]
        list includes 4 more lists of 1 bit each making them last 4 bits of 8 bit output

    '''
    x = Decoder2_4(A,B,C)
    y = Decoder2_4(NOT(A),B,C)
    return x,y
#%%

def Decoder4_16(E,A,B,C):
    '''4 to 16 Decoder
    

    Parameters
    ----------
    E : list[]
        Enable input
    A : list[]
    B : list[]
    C : list

    Returns
    -------
    result : array[:,16]
        array with all 16 bit output for each 4 bit input instance

    '''
    En = NOT(E)
    An = NOT(A)
    Bn = NOT(B)
    Cn = NOT(C)
    y0 = (AND_AND(Cn,Bn,An,En))[2]
    y1 = (AND_AND(C,Bn,An,En))[2]
    y2 = (AND_AND(Cn,B,An,En))[2]
    y3 = (AND_AND(C,B,An,En))[2]
    y4 = (AND_AND(Cn,Bn,A,En))[2]
    y5 = (AND_AND(C,Bn,A,En))[2]
    y6 = (AND_AND(Cn,B,A,En))[2]
    y7 = (AND_AND(C,B,A,En))[2]
    y8 = (AND_AND(Cn,Bn,An,E))[2]
    y9 = (AND_AND(C,Bn,An,E))[2]
    y10 = (AND_AND(Cn,B,An,E))[2]
    y11 = (AND_AND(C,B,An,E))[2]
    y12 = (AND_AND(Cn,Bn,A,E))[2]
    y13 = (AND_AND(C,Bn,A,E))[2]
    y14 = (AND_AND(Cn,B,A,E))[2]
    y15 = (AND_AND(C,B,A,E))[2]
    result=np.column_stack((y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15))
    return result

#%%
def Encoder2_1(A,B):
    '''2 to 1 encoder

    Parameters
    ----------
    A : list[]
    B : list[]

    Returns
    -------
    result : list[]

    '''
    result = OR(NOT(A),B)
    return result
#%%
def Encoder4_2(A,B,C,D):
    '''4 to 2 Encoder

    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]

    Returns
    -------
    x : list[]
    y : list[]

    '''
    x = OR(A,B)
    y = OR(A,C)
    return x,y
#%%
def Encoder8_3(A,B,C,D,E,F,G,H):
    '''8 to 3 encoder

    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]
    E : list[]
    F : list[]
    G : list[]
    H : list[]

    Returns
    -------
    x : list[]
    y : list[]
    z : list[]

    '''
    x = (OR_OR(A,B,C,D))[2]
    y = (OR_OR(A,B,C,E))[2]
    z = (OR_OR(A,C,E,G))[2]
    return x,y,z
#%%
def Priority_Enc4_2(A,B,C,D):
    '''Parity Encoder from 4 to 2 bits

    Parameters
    ----------
    A : list[]
    B : list[]
    C : list[]
    D : list[]    
    
    Returns
    -------
    x : list[]
    y : list[]
    V : list[]
        

    '''
    x = OR(A,B)
    y1 = AND(NOT(B),C)
    y = OR(A,y1)
    V = (OR_OR(A,B,C,D))[2]
    return x,y,V
#%%
















