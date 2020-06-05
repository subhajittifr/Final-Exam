import numpy as np 
import matplotlib.pyplot as plt
####Define function array of f(y1,y2,x)
def r(x,y1,y2):
    return np.array([32*y1+66*y2+(2*x)/3+2/3,-66*y1-133*y2-x/3-1/3])

h=0.01
a=0
b=0.5
y1_initial=1/3
y2_initial=1/3
n=int((b-a)/h)
t=np.linspace(a,b,n+1)
y1=[];y1.append(y1_initial)
y2=[];y2.append(y2_initial)
############## RK4 Algorithm ######################
for i in range(n):
    k1=h*r(t[i],y1[i],y2[i])
    k2=h*r(t[i]+h/2,y1[i]+k1[0]/2,y2[i]+k1[1]/2)
    k3=h*r(t[i]+h/2,y1[i]+k2[0]/2,y2[i]+k2[1]/2)
    k4=h*r(t[i]+h,y1[i]+k3[0],y2[i]+k3[1])
    y1.append(y1[i]+(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6)
    y2.append(y2[i]+(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6)
##################### PLOTTING #########################
plt.suptitle(r'$Problem \ 6$',fontsize=14)
plt.subplot(121)
plt.plot(t,y1,color = 'c')
plt.ylabel(r'$y_1$',fontsize=16)
plt.xlabel(r'$x$',fontsize=16)
plt.grid()
plt.subplot(122)
plt.plot(t,y2,color = 'maroon')
plt.ylabel(r'$y_2$',fontsize=16)
plt.xlabel(r'$x$',fontsize=16)
plt.grid()
plt.show()



