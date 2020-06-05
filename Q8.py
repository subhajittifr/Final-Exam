#Question 8: 
from scipy.integrate import solve_bvp
import numpy as np
import matplotlib.pyplot as plt
e=np.exp(1)
def f(x, y):
	return np.vstack((y[1], 4*(y[0]-x)))

def bc(ya, yb):
	return np.array([ya[0], yb[0]-2])
def y_exact(x):
	return e**2*pow((e**4-1),-1)*(np.exp(2*x)-np.exp(-2*x))+x
x=np.linspace(0,1)
y=y_exact(x)
y_dim = np.zeros((2, x.size))
sol =solve_bvp(f, bc, x, y_dim)
y_calc=sol.sol(x)[0]
err=abs((y-y_calc)/y)*100
step=[]
for i in range(len(x)):
	step.append(i)
	print('Number of step:',i+1, 'Error:',err[i])
plt.suptitle(r'$Problem \ 8$',fontsize=14)
plt.subplot(122)
plt.plot(step,err,'maroon')
plt.xlabel('Steps')
plt.ylabel('Error in each step')
plt.subplot(121)
plt.plot(x,y_calc,'tab:orange')
plt.plot(x,y,'c')
plt.ylabel(r'$y$',fontsize=16)
plt.xlabel(r'$x$',fontsize=16)
plt.legend(['solve_bvp','Analytical'])


plt.show()

				
																			