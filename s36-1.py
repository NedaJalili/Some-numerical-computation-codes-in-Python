import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
def f(x,a,b):
    return 1/(a+b*x)
x=np.linspace(0,4,40)
y=f(x,a=1.5,b=1.3)+0.02*np.random.normal(size=(40))
popt,pcov=curve_fit(f,x,y)
a,b=popt
print("a = ",a)
print("b = ",b)
ypred=f(x,a,b)

plt.plot(x,y,"o",label="data")
plt.plot(x,ypred,label="fit")
plt.legend()
plt.show()
