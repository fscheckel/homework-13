#p(x;X0,gmma)=1/(pi*gmma*[1+((x-X0)/gmma)^2])
#F(x)=(1/pi)arctan((x-X0)/gmma)+(1/2)

import numpy as np
import matplotlib.pyplot as plt

def random_cauchy(X0, gamma, h): #
    for i in range(h):
        x = np.random.random(0, 1)
        xval = [] #put the values we are going to try here
        xval.append(x)
        inverse = (1/np.pi)*np.arctan((x-X0)/gamma)+(1/2) #cdf
        inv = [] #put the solutions here
        inv.append(inverse)
    return inv

if __name__ == "__main__":
    gamma = 1
    xrange = np.arrange(-40, 40, 0.01) #limits for the values of the x-axis
    yrange = random_cauchy(X0, gamma, h) #our variables 

plt.hist(xrange, yrange)
plt.title('"fat-tail" distribution')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()