# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 15:00:29 2021

@author: Vishwesh
"""
import matplotlib.pyplot as plt
from basic_gates import AND, OR, NOT, NAND, NOR,XNOR,XOR,binary_check,length_check
from secondary_gates import AND_AND, AND_OR, AND_NAND, AND_NOR, OR_AND, OR_OR 
from secondary_gates import OR_NAND, OR_NOR, NAND_AND, NAND_OR, NAND_NAND, NAND_NOR 
from secondary_gates import NOR_AND, NOR_OR, NOR_NAND, NOR_NOR
from arithmatic_gates import half_adder,full_adder,half_subtractor,full_subtractor

#%% plots for basic gates

def plot_basic(x,y,gate):
    g=gate (x,y)
    plt.figure(1)
    plt.subplot(3, 1, 1)
    plt.xlim(0,len(x))
    plt.ylim(0,2)
    plt.ylabel("input 1")
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.1,axis='x')
    plt.plot(x)
    plt.subplot(3, 1, 2)
    plt.xlim(0,len(y))
    plt.ylim(0,2)
    plt.ylabel("input 2")
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.1,axis='x')
    plt.plot(y)
    plt.subplot(3, 1, 3)
    plt.xlim(0,len(g))
    plt.ylim(0,2)
    plt.xlabel("Instances")
    plt.ylabel("output")
    plt.plot(g,color='r')
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.1,axis='x')
    plt.show()
    return g
    
#%% plots for secondary gates

def plot_secondary(x,y,z,q,gate1,gate2):
    g=gate1 (x,y)
    h=gate1 (z,q)
    i=gate2 (g,h)
    
    plt.figure(2)
    plt.subplot(3, 1, 1)
    plt.xlim(0,len(x))
    plt.ylim(0,2)
    plt.ylabel("gate 1")
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.1,axis='x')
    plt.plot(g)
    plt.subplot(3, 1, 2)
    plt.xlim(0,len(y))
    plt.ylim(0,2)
    plt.ylabel("gate 2")
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.1,axis='x')
    plt.plot(h)
    plt.subplot(3, 1, 3)
    plt.xlim(0,len(g))
    plt.ylim(0,2)
    plt.xlabel("Instances")
    plt.ylabel("output")
    plt.plot(g,color='r')
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.1,axis='x')
    plt.show()
    return g,h,i

#%%
def plot_half_adder(A,B):
    s,c = half_adder(A,B)
    
    plt.figure(3)
    plt.subplot(2, 1, 1)
    plt.xlim(0,len(s))
    plt.ylim(0,2)
    plt.ylabel("Sum")
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.1,axis='x')
    plt.plot(s)
    plt.subplot(2, 1, 2)
    plt.xlim(0,len(c))
    plt.ylim(0,2)
    plt.ylabel("Carry")
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.1,axis='x')
    plt.xlabel("Instances")
    plt.plot(c,color='r')
    plt.show()
    return s,c    
    
#%%
def plot_full_adder(A,B,Cin):
    s,c = full_adder(A, B, Cin)
    
    plt.figure(3)
    plt.subplot(2, 1, 1)
    plt.xlim(0,len(s))
    plt.ylim(0,2)
    plt.ylabel("Sum")
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.1,axis='x')
    plt.plot(s)
    plt.subplot(2, 1, 2)
    plt.xlim(0,len(c))
    plt.ylim(0,2)
    plt.ylabel("Carry")
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.1,axis='x')
    plt.xlabel("Instances")
    plt.plot(c,color='r')
    plt.show()
    return s,c    

#%%
def plot_half_subtractor(A,B):
    difference,borrow = half_subtractor(A,B)
    
    plt.figure(3)
    plt.subplot(2, 1, 1)
    plt.xlim(0,len(difference))
    plt.ylim(0,2)
    plt.ylabel("Difference")
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.1,axis='x')
    plt.plot(difference)
    plt.subplot(2, 1, 2)
    plt.xlim(0,len(borrow))
    plt.ylim(0,2)
    plt.ylabel("Borrow")
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.1,axis='x')
    plt.xlabel("Instances")
    plt.plot(borrow,color='r')
    plt.show()
    return difference,borrow  
#%%
def plot_full_subtractor(A,B,Bin):
    difference,borrow = full_adder(A, B, Bin)
    
    plt.figure(3)
    plt.subplot(2, 1, 1)
    plt.xlim(0,len(difference))
    plt.ylim(0,2)
    plt.ylabel("difference")
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.1,axis='x')
    plt.plot(difference)
    plt.subplot(2, 1, 2)
    plt.xlim(0,len(borrow))
    plt.ylim(0,2)
    plt.ylabel("Borrow")
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.1,axis='x')
    plt.xlabel("Instances")
    plt.plot(borrow,color='r')
    plt.show()
    return difference, borrow  
#%%


