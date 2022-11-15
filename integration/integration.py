
import math as m
import matplotlib.pyplot as plt
import numpy as np
trap_list=[]
mid_list=[]
left_list=[]
right_list=[]
simp_list=[]
def f(x):
    return x + 2*x**4 + 3*x**5

val= 0     #actual value of the integral


for n in range(1,10):

    a=0  #lower limit
    b=3  #upper limit

    h= (b-a)/n #the value of difference
    s_left=0
    s_right=0
    s_mid=0
    s_trap=0.5*(f(a)+f(b))*h
    # Left-Point and Right point rule
    for i in range(n):
        s_left+=f(a+i*h)
        s_right+=f(a+(i+1)*h)
        s_mid+=f(a+(i+0.5)*h)

    mid_list.append(s_mid*h-val)


    for i in range(n-1):
        s_trap+=f(a+(i+1)*h)*h

    trap_list.append(s_trap-val)
    left_list.append(s_left*h-val)
    right_list.append(s_right*h-val)
    #print(s_left*h,"is the left point rule value\n",s_right*h,"is the value of the Right point method\n",s_mid*h,"is the value of mid point method.")

    #print(s_trap,"is is the value from trapizoid rule value")
    #print(" ")


    "Simpson 1/3 rule"

    
    s_simp = 0
    
    m=n

    if m%2!=0:
        m=m-1
        s_simp+=(f(b)+f(b-h))*h/2

    s_simp+=(f(a)+f(a+h*m))*h/3


    for i in range(1,m,2):
        s_simp+=4*f(a+i*h)*h/3
    for i in range(2,m-1,2):
        s_simp+=2*f(a+i*h)*h/3

    simp_list.append(s_simp-val)
    
   

#print(trap_list[-1],left_list[-1],simp_list[-1])
#print(simp_list)
trap_list=np.array(trap_list)
mid_list=np.array(mid_list)
left_list=np.array(left_list)
right_list=np.array(right_list)
simp_list=np.array(simp_list)

trap_list=np.abs(trap_list)
mid_list=np.abs(mid_list)
left_list=np.abs(left_list)
right_list=np.abs(right_list)
simp_list=np.abs(simp_list)

log_trap=np.log(trap_list)
log_mid=np.log(mid_list)
log_right=np.log(right_list)
log_left=np.log(left_list)
log_simp=np.log(simp_list)

plt.plot(mid_list,label="mid_point")
plt.plot(trap_list,label="trapizoidal")
plt.plot(left_list,label="left_point")
plt.plot(right_list,label="right_point")
plt.plot(simp_list,label="simpsion1/3")

plt.legend()

plt.grid()
plt.show()