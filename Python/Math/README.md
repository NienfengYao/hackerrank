# Python/Math

* Ref:
  * [wiki: 複數](https://zh.wikipedia.org/wiki/%E5%A4%8D%E6%95%B0_(%E6%95%B0%E5%AD%A6))

  * [cmath — Mathematical functions for complex numbers](https://docs.python.org/3.6/library/cmath.html)
    * A Python complex number z is stored internally using rectangular or Cartesian coordinates. It is completely determined by its real part z.real and its imaginary part z.imag. In other words: z == z.real + z.imag*1j

    * Polar coordinates give an alternative way to represent a complex number. In polar coordinates, a complex number z is defined by the modulus r and the phase angle phi. The modulus r is the distance from z to the origin, while the phase phi is the counterclockwise angle, measured in radians, from the positive x-axis to the line segment that joins the origin to z.

    * cmath.polar(x)
      * Return the representation of x in polar coordinates. Returns a pair (r, phi) where r is the modulus of x and phi is the phase of x.
      * polar(x) is equivalent to (abs(x), phase(x)).

  * [math — Mathematical functions](https://docs.python.org/3.6/library/math.html)
    * math.atan(x)
      * Return the arc tangent of x, in radians.

    * math.atan2(y, x)
      * Return atan(y / x), in radians. The result is between -pi and pi. The vector in the plane from the origin to point (x, y) makes this angle with the positive X axis. The point of atan2() is that the signs of both inputs are known to it, so it can compute the correct quadrant for the angle. For example, atan(1) and atan2(1, 1) are both pi/4, but atan2(-1, -1) is -3*pi/4.

    * math.degrees(x)
      * Convert angle x from radians to degrees.

  * [Built-in Functions](https://docs.python.org/3/library/functions.html#round)
    * round(number[, ndigits])
      * Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.
