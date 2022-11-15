import int_function as ig
import math

def f(x):
    return math.sin(x)
a=0
b=3
n=10
print(ig.int_mid(f,a,b,n),ig.int_trap(f,a,b,n),
ig.int_simp(f,a,b,n),ig.int_romb_first(f,a,b,n),ig.int_romb_n(f,a,b,n,2),
ig.int_gsquad_deg3(f,a,b),ig.int_gsquad_bypart(f,a,b,n))