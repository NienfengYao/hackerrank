import math

"""
math — Mathematical functions(https://docs.python.org/3.6/library/math.html)

math.atan(x)
	Return the arc tangent of x, in radians.

math.atan2(y, x)
	Return atan(y / x), in radians. The result is between -pi and pi. 
	The vector in the plane from the origin to point (x, y) makes this angle with the positive X axis.
	The point of atan2() is that the signs of both inputs are known to it, so it can compute the correct quadrant for the angle. 
	For example, atan(1) and atan2(1, 1) are both pi/4, but atan2(-1, -1) is -3*pi/4.


math.degrees(x)
	Convert angle x from radians to degrees.

round(number[, ndigits])
	Return number rounded to ndigits precision after the decimal point. 
	If ndigits is omitted or is None, it returns the nearest integer to its input.
"""

ab, bc = int(input()), int(input())
# print(ab, bc)
print(round(math.degrees(math.atan2(ab, bc))), chr(176), sep='')
