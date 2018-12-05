# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

""" First Test
N = int(input())
Rec = namedtuple('Rec', input())
sum_marks = 0
for i in range(N):
    sum_marks += int(Rec._make(input().split()).MARKS)
print("%0.2f" % (sum_marks/N))
"""

(n, categories) = (int(input()), input().split())
Grade = namedtuple('Grade', categories)
marks = [int(Grade._make(input().split()).MARKS) for _ in range(n)]
print("%0.2f" % (sum(marks) / len(marks)))
