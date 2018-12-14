# Python/Numpy

* Basic mathematical functions operate element-wise on arrays (a and b are numpy.array)
  * a + b = numpy.add(a, b)
  * a - b = numpy.subtract(a, b)
  * a * b = numpy.multiply(a, b)
  * a / b = numpy.divide(a, b)
  * a % b = numpy.mod(a, b)
  * a ** b = numpy.power(a, b)

* The output format issue can be solved by numpy.set_printoptions()
  * sign : string, either ‘-‘, ‘+’, or ‘ ‘, optional
    * Controls printing of the sign of floating-point types. If ‘ ‘, always prints a space in the sign position of positive values.
  * legacy : string or False, optional
    * If set to the string ‘1.13’ enables 1.13 legacy printing mode. This approximates numpy 1.13 print output by including a space in the sign position of floats and different behavior for 0d arrays.
    * New in version 1.14.0.

* ToDo
  * What is dot product and corss product? Especially in matrix.
    * [Dot and Cross](https://www.hackerrank.com/challenges/np-dot-and-cross/problem)
  * Inner and Outter
  * Polynomials
  * Algebra
