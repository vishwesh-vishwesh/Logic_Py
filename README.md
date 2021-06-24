# Logic_Py

[![Made with Python3](https://img.shields.io/badge/Made%20With-Python3-green)](https://www.python.org/)
[![GitHub license](https://img.shields.io/badge/license-Apache2.0-blue.svg)](https://github.com/vishwesh-vishwesh/Logic_Py/blob/main/LICENSE)
[![Github version](https://img.shields.io/badge/version-0.4.1-green)](https://github.com/vishwesh-vishwesh/Logic_Py)

### *Update : Logic_Py 0.4.1*

1. If input array contains a non-binary element, A ValueError is returned with the exact location of non-binary element in the input array
```python
from basic_gates import AND
A = [1,0,1,3]
B = [0,0,1,1]
y = AND(A,B)
```
 Above code returns `ValueError: input must be binary, 0 or  1 in first input index 3`

2. If all the input array lengths are not same, Again code throws a ValueError
```python
from basic_gates import OR
A = [1,0,1]
B = [0,0,1,1]
y = OR(A,B)
```
 Above code returns `ValueError: Length of both inputs must be same`

3. Half subtractor and Full subtractor are added to Arithmatic gates
```python
from arithmatic_gates import half_subtractor, full_subtractor
B = [1,1,0,1,1,0,0,1,0,0]
A = [0,0,0,1,0,1,1,0,1,1]
Difference, Borrow = half_subtractor(A,B)
print("Difference : ", Difference, "Borrow : ", Borrow)
```
 Above snippet returns Difference :  `Difference :  [1, 1, 0, 0, 1, 1, 1, 1, 1, 1] Borrow :  [0, 0, 0, 0, 0, 1, 1, 0, 1, 1]`

4. Code conversions BCD to Excess3 and vice versa are added to Combinational circuits
```python
from combinational_gates import BCD2Excess3, Excess32BCD
A = [1,1,0,1,1,0,0,1,0,0]
B = [0,0,0,1,0,1,1,0,1,1]
C = [0,1,0,1,0,1,0,0,0,0]
D = [1,1,0,1,1,0,0,1,0,0]
w,x,y,z = BCD2Excess3(A,B,C,D)
```
 Above code saves 4 coverted Excess3 bits in w,x,y,z

5. Encoders and Decoders are added to Logic circuits
```python
from Logic_circuits import Decoder2_4,Decoder4_16,Decoder3_8,Encoder2_1,Encoder4_2,Encoder8_3,Priority_Enc4_2
```
6. Plots are added for half subtractor and full subtractor
 ```python
from plotting import plot_half_subtractor
x,y = plot_half_subtractor(B,C)
```
 Above snippet returns a plot of difference and Borrow and also loads difference and borrow onto the variables x and y.
![Half Subtractor](https://github.com/vishwesh-vishwesh/Logic_Py/blob/main/Figure%202021-06-24%20073914.png "Half subtractor")


# Introduction
This Python package enables the user to realise Logic based combinational circuits built on basic logic gates.
All the inputs must be binary and of same length for the functions to perform desired operation. 

## Installation
`pip install logic-py`
```python
from Logic_Py import AND, full_adder, plot_secondary
```

## Basic Gates
`basic_gates`

There are 7 basic gates, all other secondaary and combinational gates are the combinations of these 7 basic gates.
- AND, OR, NOT, NAND, NOR,XNOR,XOR
```python
from Logic_Py import AND
```

## Secondary Gates
`secondary_gates`

There are 16 Secondary gates, which take 4 binary inputs and 1 binary output.
- AND_AND, AND_OR, AND_NAND, AND_NOR, OR_AND, OR_OR, OR_NAND, OR_NOR, NAND_AND, NAND_OR, NAND_NAND, NAND_NOR, NOR_AND, NOR_OR, NOR_NAND, NOR_NOR,

## Combinational Gates
`combintional_gates`

Few combinational circuits are added as start in this beta version, few more will follow in the coming update.
- Binary2Gray, Gray2Binary, EParity_gen, EParity_check, OParity_gen, OParity_check, Excess32BCD, BCD2Excess3

## Arithmatic Gates
`arithmatic_gates`
Two arithmatic gates are added for the beta version, more will follow in the coming update.
*update 0.4.1 added subtractors*
- Half Adder - `half_adder`
- Full Adder - `full_adder`
- Half Subtractor - `half_subtractor`
- Full Subtractor - `full_subtractor`

## Plots
`plotting`

Plots for the basic gates, secondary gates and arithmatic gates are available with the current version.
- plot_full_adder, plot_half_adder, plot_secondary, plot_basic
- *update 0.4.1 added `plot_half_adder` and `plot_full_adder`

## Citation
- [Tutorialspoint - digital circuit basics](https://www.tutorialspoint.com/digital_circuits)
- [Geeksforgeeks digital circuits](https://www.geeksforgeeks.org/)

>Use [Github](https://github.com/vishwesh-vishwesh/Logic_Py/) for further updates. 
>Please kindly cite incase you use the package and fork.

>Use Hellow world example for the syntax
>or use help function in python console
```python
help(AND)
```

