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
from plotting import plot_full_adder, plot_half_adder, plot_secondary, plot_basic