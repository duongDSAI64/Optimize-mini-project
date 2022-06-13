import time
import numpy as np
import sys
def input(filename):
    global N,student,R,room,a,conflict
    with open(filename) as f:
        N=int(f.readline())
        student=np.array(f.readline().split(' '),dtype='int')
        R=int(f.readline())
        room=np.array(f.readline().split(' '),dtype='int')
        a=int(f.readline())
        conflict=np.array([[int(num) for num in line.split()] for line in f])
input('data50.txt')
n_shift=int((N//R)*R+6)     # number of shifts             
shift=[None]*n_shift
subject=[i+1 for i in range(n_shift)]
student=list(student)
student = student+(n_shift-N)*[0]

conflict_table=np.zeros((n_shift,n_shift),dtype='int')      # conflict table
for i in range(a):
    conflict_table[conflict[i,0],conflict[i,1]]=1
    conflict_table[conflict[i,1],conflict[i,0]]=1

def print_solu(arr):
    for j in range(len(arr)):
        if arr[j]>N:
            arr[j]=None           
    for i in range(int(n_shift/3)):
        print(arr[3*i:3*i+3])
        
def check(v,x):
    if subject[v] in shift[0:x]:
        return False
    if student[v]>room[x%3]:
        return False
    if x%3==1 and conflict_table[shift[x-1]-1,v]==1:
        return False
    if x%3==2 and (conflict_table[shift[x-2]-1,v]==1 or conflict_table[shift[x-1]-1,v]==1):
        return False
    return True

def Try(x):
    global N
    for v in range(n_shift):
        if check(v,x):
            shift[x]=subject[v]
            if x>=n_shift-1:
                print_solu(shift)
                sys.exit()
            else:
                Try(x+1)
Try(0)