# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 17:48:10 2021

@author: Vishwesh
"""
import numpy as np
from basic_gates import OR, AND
from plotting import plot_basic
from combinational_gates import *
from Logic_circuits import *
from arithmatic_gates import *
w = [1,1,0,1,1,0,0,1,0,0]
x = [0,0,0,1,0,1,1,0,1,1]
y = [0,1,0,1,0,1,0,0,0,0]
z = [1,1,0,1,1,0,0,1,0,0]

#%%
s = Priority_Enc4_2(w,x,y,z)

#%%
g = full_subtractor(w,x,y)

#%%
l = Decoder4_16(w,x,y,z)
#%%
m,n,o,p = BCD2Excess3(w,x,y,z)

#%%
q,p,r,s = Excess32BCD(w,x,y,z)
#%%
plot_basic(x, y, AND)

#%%
from arithmatic_gates import full_adder
from plotting import plot_full_adder

sum_,carry_ = full_adder(x, y,z)
plot_full_adder(x,y,z)

#%%






