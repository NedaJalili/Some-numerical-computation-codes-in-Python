import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(v,t):
    return 10*t
v0=1
t=np.linspace(0,5,100)
v=odeint(f,v0,t)
plt.plot(t,v)
plt.xlabel("t")
plt.ylabel("v")
plt.show()
