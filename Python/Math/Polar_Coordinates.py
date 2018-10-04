import cmath

"""
A Python complex number z is stored internally using rectangular or Cartesian coordinates.
It is completely determined by its real part z.real and its imaginary part z.imag.
In other words:
z == z.real + z.imag*1j
"""

z = complex(input())
# print(z)
"""
cmath.polar(x)
    Return the representation of x in polar coordinates.
    Returns a pair (r, phi) where r is the modulus of x and phi is the phase of x. 
    polar(x) is equivalent to (abs(x), phase(x)).
"""
print(cmath.polar(z)[0])
print(cmath.polar(z)[1])
