import numpy as np 
import matplotlib.pyplot as plt 
def f(x):#Definition of the function
    if abs(x)<=1:
        sol=1
    else:
        sol=0
    return sol

def g(n):
    N=2**n
    x=np.linspace(x_min,x_max,N)
    delta = (x_max-x_min)/(N-1)
    f_arr,fk_arr_exact=[],[]
    for i in range(N):
        f_arr.append(f(x[i]))
    n_fft = np.fft.fft(f_arr, norm='ortho') 
    k_arr = np.fft.fftfreq(N, d=delta)
    karr = 2*np.pi*k_arr
    factor = np.exp(-1j * karr * x_min)
    aft = np.real(delta * np.sqrt(N/(2.0*np.pi)) * factor * n_fft)
    return np.array([karr,aft,delta])
x_min=-50
x_max=50
x1=np.linspace(-5,5,100)
fx=[]
for i in range(len(x1)):
    fx.append(f(x1[i]))
plt.suptitle(r'$Problem \ 10$',fontsize=14)
plt.subplot(121)
plt.plot(x1,fx,label=r'$f(x)$')
plt.xlabel(r'$x$',fontsize=20)
plt.ylabel(r'$f(x)$',fontsize=20)
plt.subplot(122)
plt.plot(g(9)[0],g(9)[1],color='salmon',label = 'n=9')
plt.plot(g(10)[0],g(10)[1],color='c',label = 'n=10')
plt.plot(g(12)[0],g(12)[1],color='maroon',label = 'n=12')
plt.text(50,0.4, r"$\Delta=\frac{100}{2^n-1}$",color='k',fontsize=14)
plt.xlabel(r'$k$',fontsize=20)
plt.ylabel(r'$\tilde{f}(k)$',fontsize=20)
plt.legend()
# plt.grid()
plt.show()