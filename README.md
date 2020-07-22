# PySuperDecimal
This repository contains files for a simple Python data type named PySuperDecimal. Below shows information about how to use PySuperDecimal and the 
source code and tests for it.

### Addition

>>> PySuperDecimal("5.13") + PySuperDecimal("4.69")
9.82

### Subtraction

>>> PySuperDecimal("5.13") - PySuperDecimal("4.69")
0.44

### Multiplication

>>> PySuperDecimal("5.13") * PySuperDecimal("4.69")
24.0597

### Division

>>> PySuperDecimal("5.13") / PySuperDecimal("4.69")
1.09381663113006

### Integer Division

>>> PySuperDecimal("5.13") // PySuperDecimal("4.69")
1

### Modulus

>>> PySuperDecimal("8") // PySuperDecimal("3")
2

### Exponent
>>> PySuperDecimal("2") // PySuperDecimal("3")
8

### Sine
>>> sin(PySuperDecimal(str(math.pi / 2)))
1.0

### Cosine
>>> cos(PySuperDecimal(str(0)))
1.0

## Tangent
>>> tan(PySuperDecimal(str(0)))
0

### Cosecant
>>> cosec(PySuperDecimal(str(math.pi / 2)))
1.0

### Secant
>>> sec(PySuperDecimal(str(0)))
1.0

### Cotangent
>>> cot(PySuperDecimal(str(math.pi / 4)))
1.0

### Hyperbolic Sine
>>> sinh(PySuperDecimal(str(math.pi / 2)))
2.3012989023073

### Hyperbolic Cosine
>>> cosh(PySuperDecimal(str(math.pi / 2)))
2.50917847865806

### Hyperbolic Tangent
>>> tanh(PySuperDecimal(str(math.pi / 2)))
0.917152335667275

### Hyperbolic Cosecant
>>> cosech(PySuperDecimal(str(math.pi / 2)))
0.434537208094695

### Hyperbolic Secant
>>> sech(PySuperDecimal(str(math.pi / 2)))
0.398536815338386

### Hyperbolic Cotangent
>>> coth(PySuperDecimal(str(math.pi / 2)))
1.09033141072737

### Square Root
>>> sqrt(PySuperDecimal("6.25"))
2.5
