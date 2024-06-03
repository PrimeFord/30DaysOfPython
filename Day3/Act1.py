import math
#My age
age = int(32)
height = float(5.11)
complex = (5+2j)

#Area triangle
base = input ('base: ')
height = input ('height: ')
area = 0.5 * int(base) * int(height)
print(area)

#Perimeter Triangle
a = input ('side a: ')
b = input ('side b: ')
c = input ('side c: ')
perimeter = int(a) + int(b) + int(c)
print(perimeter)

#Perimeter Rectangle & Area Rectangle
length = input ('length: ')
width = input ('width: ')
periRec = 2 * (int (length) + int(width))
print(periRec)
areaRec = int(length) * int(width)
print(areaRec)

#Circumfrence and Area of circle
#Input radius
radius = input ('radius: ')

pi = 3.14
circumfrence = 2 * pi * int(radius)
print(circumfrence)
area = pi * (int(radius) ** 2)
print(area)
#Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope = 2  # the m in y=mx +c by comparison m=2
#x intercept
"""
let y=0 so the point is (x,0)
using the slope equation
0=2x -2
2x=2
x=1
"""
x = 1

#y intercept
"""
let x=0 so the point is (0,y)
using the slope equation
y=2(0)+2
y=2
"""
y = 2 

print("Slope: ", slope)
print("X intercept: ", x)
print("Y intercept: ", y)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
sslope = (10-2)/(6-2)
print('Slope: ',sslope)
#euclidean distance
eucl = math.sqrt((2-2)+(10-6))
print('Eucleadean distance: ',eucl)

# comparing the two slopes
print(slope==sslope)
print('task 8 slope is task 9 slope: ', slope is sslope)

#Calculate the value of y (y = x^2 + 6x + 9) use a value that will make y=0
xx = input('value for x to get y=0 enter -3: ')
yy = (int(xx)**2) + (6*int(xx)) + 9
print('y is:',yy)

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
py= len("python")
dg = len("dragon")
print('pyhton length: ', py)
print('dragon length: ', dg)
print("falsify the statement", py != dg)
print("falsify the statement", py is not dg)

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
ispy= "on" in "python"
isdg= "on" in "dragon"
print("Is on in python: ", ispy)
print("Is on in dragon: ", isdg)
print("using the and operator to check if on is in dragon and python: ", ispy and isdg)

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
jarg="I hope this course is not full of jargon."

print("Is jargon in jarg","jargon:" in jarg )