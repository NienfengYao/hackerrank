class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
        
    def calculate(self):
        avg = sum(self.scores) / len(self.scores)
        if (avg >= 90):
            return 'O'
        elif (avg >= 80):
            return 'E'
        elif (avg >= 70):
            return 'A'
        elif (avg >= 55):
            return 'P'
        elif (avg >= 40):
            return 'D'
        else:
            return 'T'

# for modify the behavior of printf
import builtins
def print(*args,**kwargs):
    if "sep" not in kwargs and args[0] =="Grade: ":
        builtins.print(*args,**kwargs,sep="")
    else:
        builtins.print(*args,**kwargs)

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade: ", s.calculate())
