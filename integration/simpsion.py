# Program for integration using simpsion 1/3
import matplotlib.pyplot as plt


def f(x):
    return (x**2+x)**2

a=-5   #starting value
b=10   #end value
l=b-a   #limit of the integration

simp_list=[]

for n in range(1,100):
    #n=9   #numbers of segment to be devided
    h=l/n   #increment


    m=n 
    s_simp=0

    if m%2 != 0:
        m= m-1
        s_simp+= (f(b)+f(b-h))*h/2 
    
    s_simp+=(f(a)+f(a+m*h))*h/3



    for i in range(1,m,2):
        s_simp+=4*f(a+i*h)*h/3
    for i in range(2,m-1,2):
        s_simp+=2*f(a+i*h)*h/3

    simp_list.append(s_simp-9)

print(simp_list)

plt.plot(simp_list,label="simpson1/3")
plt.grid()
plt.show()