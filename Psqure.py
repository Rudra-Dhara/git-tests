import numpy as np
def square(n):
    return float(n)*float(n)

a = np.array([ls1,2,3,4,5])
c=[1,2,3]
b = float(input("Enter a number to square: "))
print('The square of the array',a,"is ",square(a),
"\nand the square of the number ",b,"is ",square(b))
print(square(c))