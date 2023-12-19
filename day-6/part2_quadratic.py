import cmath
import math

f = open("day-6/input.txt")
data = f.read()

time, distance = [int(line.split(":")[1].replace(" ", "")) for line in data.split("\n")]

quadratic = cmath.sqrt(time**2 - 4 * 1 * distance)
root1 = (-time + quadratic) / (2 * 1)
root2 = (-time - quadratic) / (2 * 1)

print(math.ceil(root1.real - root2.real))
