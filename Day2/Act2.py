
#Excercise One
import math


num_one=5
num_two=4

#Sum
total=num_one+num_two
print(total)

#diff
diff = num_one - num_two
print(diff)

#Product
product = num_one * num_two
print(product)

#division
division =num_one / num_two
print(division)

#modulus
remainder = num_one % num_two
print(remainder)

#exp
exp = num_one ** num_two
print(exp)

#floor
floor =num_one // num_two
print(floor)

# Radius of a circle =30 meters
radius = 30
#Area of circle
area = math.pi * (radius ** 2)
print(area)
#Circumfrence of circle
circumfrence = 2 * math.pi * radius
print(circumfrence)
#Input radius
radii = input('radius: ')
inputarea = math.pi * (int(radii) ** 2)
print(inputarea)