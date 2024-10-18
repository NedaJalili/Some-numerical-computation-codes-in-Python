from scipy.integrate import quad
import numpy as np
def f(x):
    return (np.cos(x)**2)*np.sin(x)
a=0
b=np.pi/2
s=quad(f,a,b)
print("f(x)=",s)

def f2(y):
    return y*np.exp(2*y)
c=0
d=1
s2=quad(f2,c,d)
print("f2(x)=",s2)

def f3(z):
    return np.log(z)/z
s3=quad(f3,2,3)
print("f3(x)=",s3)
