import numpy as np

def SVD(A):
	U1,S1,V1=np.linalg.svd(A)
	return S1
A=[
   [2,1],
   [1,0],
   [0,1]]
B=[
   [1,1,0],
   [1,0,1],
   [0,1,1]]



print('After performing SVD we obtain the singular values of matrix 1:')
print(SVD(A))
print('After performing SVD we obtain the singular values of matrix 2:')
print(SVD(B))









