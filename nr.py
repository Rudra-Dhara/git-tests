import matplotlib.pyplot as plt
def f(x):
    return x**2-9
def df(x):
    return 2*x

#defining the range within to search the root
x=[-1]

for i in range(100):
    
    x.append(x[i] - f(x[i])/df(x[i]))
    if abs((x[i]-x[i+1]))<0.0001:
        break
    
print("The value of the root is:",x)

plt.plot(x)
plt.show()