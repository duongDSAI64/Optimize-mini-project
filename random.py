import numpy as np
from numpy import random
N=500
A=np.zeros(N,dtype='int')
for i in range(N):
    A[i]=random.randint(0,50)
print(N)
print(*A)

R=5
room=np.zeros(R,dtype='int')
for i in range(R):
    room[i]=int(random.randint(3,6)*10)
print(R)
print(*room)

S=400
print(S)
conflict=np.zeros((S,2),dtype='int')
for i in range(S):
    for j in range(2):
        conflict[i,j]=random.randint(N)+1
for i in conflict:
    print(*i)
