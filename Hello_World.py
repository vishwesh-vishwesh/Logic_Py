# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 17:48:10 2021

@author: Vishwesh
"""
from basic_gates import AND
from plotting import plot_basic

x = [1,0,0,1,0,1,1,0,1,0]
y = [0,1,0,1,0,1,0,1,0,0]
z = [1,1,0,1,1,0,0,1,0,0]

result = AND (x,y)
plot_basic(x, y, AND)

#%%
from arithmatic_gates import full_adder
from plotting import plot_full_adder

sum_,carry_ = full_adder(x, y, z)
plot_full_adder(x,y,z)

#%%