import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
def f(x,a,b):
    return np.asin(a*x+b)
x=np.linspace(0,2*np.pi,100)
y=f(x,a=1.5,b=1.3)+0.02*np.random.normal(size=len(100))
popt,pcov=curve_fit(f,x,y)
a,b=popt
print("a = ",a)
print("b = ",b)
ypred=f(x,a,b)

plt.plot(x,y,"o",label="data")
plt.plot(x,ypred,label="fit")
plt.legend()
plt.show()
