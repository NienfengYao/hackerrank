class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        self.maximumDifference = 0
        for i in self.__elements:
            for j in self.__elements:
                if(self.maximumDifference < abs(i - j)):
                    self.maximumDifference = abs(i-j)

# End of Difference class
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
