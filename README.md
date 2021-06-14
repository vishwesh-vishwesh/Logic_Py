# Logic_Py

[![Made with Python3](https://img.shields.io/badge/Made%20With-Python3-green)](https://www.python.org/)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/vishwesh-vishwesh/Logic_Py/blob/main/LICENSE)
[![Github version](https://img.shields.io/badge/version-0.3.4-green)](https://github.com/vishwesh-vishwesh/Logic_Py)

This Python package enables the user to realise Logic based combinational circuits built on basic logic gates.
All the inputs must be binary and of same length for the functions to perform desired operation. 

## Installation
- pip install logic-py
- from Logic_Py import AND, full_adder, plot_secondary etc.,

## Basic Gates

There are 7 basic gates, all other secondaary and combinational gates are the combinations of these 7 basic gates.
- AND, OR, NOT, NAND, NOR,XNOR,XOR
- ex : from Logic_Py import AND

## Secondary Gates

There are 16 Secondary gates, which take 4 binary inputs and 1 binary output.
- AND_AND, AND_OR, AND_NAND, AND_NOR, OR_AND, OR_OR, 
   OR_NAND, OR_NOR, NAND_AND, NAND_OR, NAND_NAND, 
   NAND_NOR, NOR_AND, NOR_OR, NOR_NAND, NOR_NOR,

## Combinational Gates
Few combinational circuits are added as start in this beta version, few more will follow in the coming update.
- Binary2Gray, Gray2Binary, EParity_gen, EParity_check, OParity_gen, OParity_check

## Arithmatic Gates
Two arithmatic gates are added for the beta version, more will follow in the coming update.
- Half Adder
- Full Adder

## Plots
Plots for the basic gates, secondary gates and arithmatic gates are available with the current version.
- plot_full_adder, plot_half_adder, plot_secondary, plot_basic

## Citation
- [Tutorialspoint - digital circuit basics](https://www.tutorialspoint.com/digital_circuits)

>Use [Github](https://github.com/vishwesh-vishwesh/Logic_Py/) for further updates. 
>Please kindly cite incase you use the package and fork.

>Use Hellow world example for the syntax
>or use help function in python console
>ex: help(AND)

