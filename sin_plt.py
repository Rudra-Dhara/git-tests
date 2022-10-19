import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,2*np.pi,100)

plt.plot(x,np.sin(x))
plt.xlabel("theta in radian")
plt.ylabel("Sin x")
plt.title("Sin(x)")
plt.grid()
plt.show()