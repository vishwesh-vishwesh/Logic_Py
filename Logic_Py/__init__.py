# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 17:34:19 2021

@author: Vishwesh
"""
from basic_gates import AND, OR, NOT, NAND, NOR,XNOR,XOR
from secondary_gates import AND_AND, AND_OR, AND_NAND, AND_NOR, OR_AND, OR_OR 
from secondary_gates import OR_NAND, OR_NOR, NAND_AND, NAND_OR, NAND_NAND, NAND_NOR 
from secondary_gates import NOR_AND, NOR_OR, NOR_NAND, NOR_NOR
from arithmatic_gates import half_adder,full_adder
from combinational_gates import Binary2Gray, Gray2Binary,EParity_gen,EParity_check,OParity_gen,OParity_check
from plotting import plot_full_adder, plot_half_adder, plot_secondary, plot_basic
#%% update 2
from combinational_gates import Excess32BCD
from Logic_circuits import Decoder2_4,Decoder4_16,Decoder3_8,Encoder2_1,Encoder4_2,Encoder8_3,Priority_Enc4_2
from arithmatic_gates import half_subtractor,full_subtractor
from plotting import plot_full_subtractor,plot_half_subtractor

#%%