import numpy as np 
import matplotlib.pyplot as plt
y=np.random.uniform(0,1,1024)
x=np.linspace(0,1,1024)
N=len(x)
print(N)
delta=1/(N-1)
nft=np.fft.fft(y,norm='ortho')  ##performing DFT
k=2*np.pi*np.fft.fftfreq(N, d=1)  ## Sampling wavefactor k
power_spec=[]
for i in range(N):
	k1=(1/N)*(np.absolute(nft[i]))**2
	power_spec.append(k1)
k_min=np.amin(k)
k_max=np.amax(k)
print('Part(c):')
print('Minimum value of k',k_min)
print('Maximum value of k',k_max)
##############################################################
plt.subplots()
plt.scatter(x,y)
plt.ylabel(r'$PDF$',fontsize=16)
plt.xlabel(r'$x$',fontsize=16)
plt.title(r'$Part\ (a):$',fontsize=16)
plt.subplots()
plt.plot(k,power_spec)
plt.title(r'$Power  \ Spectra \ Part\ (b):$',fontsize=16)
plt.xlabel(r'$k_q$',fontsize=16)
plt.ylabel(r'$\frac{1}{N} |\tilde{f}(k_q)|^2$',fontsize=16)
plt.subplots()
plt.hist(power_spec,range=(k_min,k_max),bins=5,density='true',color="maroon",label='Histogram')
plt.xlabel(r'$bins$',fontsize=16)
plt.ylabel(r'$\frac{1}{N} |\tilde{f}(k_q)|^2$',fontsize=16)
plt.title(r'$Part\ (d):$',fontsize=16)
plt.show()