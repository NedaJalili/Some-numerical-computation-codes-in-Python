from scipy.optimize import minimize
import numpy as np
def f(x):
    return x+np.exp(-x)
mymin=minimize(f,0,method="BFGS")
print(mymin)
