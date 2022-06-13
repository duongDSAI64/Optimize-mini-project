import numpy as np
import time

#INPUT
def input(filename):
    global N,student,R,room,a,conflict
    with open(filename) as f:
        N=int(f.readline())
        student=np.array(f.readline().split(' '),dtype='int')
        R=int(f.readline())
        room=np.array(f.readline().split(' '),dtype='int')
        a=int(f.readline())
        conflict=np.array([[int(num) for num in line.split()] for line in f])
input('data500.txt')

conflict_table=np.zeros((N,N),dtype='int')      # conflict table
for i in range(a):
    conflict_table[conflict[i,0]-1,conflict[i,1]-1]=1
    conflict_table[conflict[i,1]-1,conflict[i,0]-1]=1

def safe(x,y):                  # check conflict
    if y==-1 or x==-1:
        return True
    else:
        if conflict_table[x,y]==0:
            return True
        else:
            return False
def safe_shift(x,arr):          # check shift
    if len(arr)==1:
        return safe(x,arr[0])
    else:
        return safe(x,arr[len(arr)-1]) and safe_shift(x,arr[0:len(arr)-1])      
def greedy():
    shift=np.array([[-1]*R]*N)
    check=np.zeros(N,dtype='int')
    for i in range(N):
        for j in range(R):
            Min=9999
            mark=-1
            for k in range(N):                
                if check[k]==0 and safe_shift(k,shift[i]) and room[j]-student[k]>=0 and room[j]-student[k]<Min:
                    mark=k
                    Min=room[j]-student[k]
            shift[i,j]=mark
            check[mark]=1
    return shift

def print_solu(a):
    for i in range(len(a)//4):
        print('Day %d:' %(i+1),'\n-------')
        for j in range(4):
            print(' Period %d:' %(j+1))
            for k in range(R):
                print('  Room %d:' %(k+1),a[4*i+j,k])
    print('============')
    print('Total:',len(a)//4,'days')
start=time.time()
solu=greedy()
for i in range(N):
    for j in range(R):
        solu[i,j]+=1
tab=[]
for i in range(N):
    if solu[i].any(0):
        tab.append(solu[i])
if len(tab)%4 !=0:
    tab+=[[0]*R]*(4-len(tab)%4)
tab=np.array(tab)
print_solu(tab)
end=time.time()
print('time=',end-start,'s')
