#squares all numbers provided in input data set and gives output, using for loop
def square(lst):
    for idx in range(len(lst)):
        lst[idx] = lst[idx]**2
    return lst

#importing math module to display the value of pi
#others include sin, sinh, sqrt, tan, tau, trunc, values
import math
print("The approximation for the value of pi is",math.pi)

#
