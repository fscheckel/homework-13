#I={1 0} (x^(-(1/2)))/(e^x+1)dx
#I~= (1/N) {{n I=1} (f(xi))/(w(xi)) {b a} w(x)dx
#p(x)=1/(2(x^(1/2)))

import numpy as np
import matplotlib.pyplot as plt

def values():
x = np.random.random()
return x**2 #get random square number

def f(N):
total = 0
for i in range(N):
x = def values()
value = 1/(np.exp(x)+1))**2 #thee equation
total += value
return total

if __name__ == "__main__":
N = 1000000 #try 1 million times
print('the value is ', total)

