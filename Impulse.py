import numpy as np
import matplotlib.pyplot as plt

n= 1000
t = np.linspace(-np.pi*6,6*np.pi,n)
df = 0.1
f_0 = 0
f_max = 100000
delta = np.zeros(n)


for f in range(int((f_max-f_0)/df)):
    delta = delta+np.sin(f*df*t)+np.cos(f*df*t)

plt.plot(t,delta)
plt.show()
