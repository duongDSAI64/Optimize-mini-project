import numpy as np

def input(filename):
    global N,student,R,room,a,conflict
    with open(filename) as f:
        N=int(f.readline())
        student=np.array(f.readline().split(' '),dtype='int')
        R=int(f.readline())
        room=np.array(f.readline().split(' '),dtype='int')
        a=int(f.readline())
        conflict=np.array([[int(num) for num in line.split()] for line in f])
input('data200.txt')
conflict_table=np.zeros((N,N),dtype='int')      # conflict table
for i in range(a):
    conflict_table[conflict[i,0]-1,conflict[i,1]-1]=1
    conflict_table[conflict[i,1]-1,conflict[i,0]-1]=1

high=[]                                     #classify
med=[]
low=[]
for i in range(N):
    if student[i]>40:
        high.append(i+1)
    elif student[i]<=30:
        low.append(i+1)
    else:
        med.append(i+1)

def safe(x,y):                  # check conflict
    if y==None or x==None:
        return True
    else:
        if conflict_table[x-1,y-1]==0:
            return True
        else:
            return False
        
def greedy():
    shift=np.array([[None]*R]*N)
    check=np.zeros(N,dtype='int')
    for i in range(len(high)):
        shift[i,1]=high[i]
        check[high[i]-1]= 1
    for j in range(N):
        for m in med:
            if check[m-1]==0 and safe(shift[j,1],m):
                shift[j,0]=m
                check[m-1]=1
                break
    for k in range(N):
        for l in low:
            if check[l-1]==0 and safe(shift[k,1],l) and safe(shift[k,0],l):
                shift[k,2]=l
                check[l-1]=1
                break                      
    return shift

def print_solu(a):
    for i in range(len(a)//4):
        print('Day %d:' %(i+1),'\n--------')
        for j in range(4):
            print(' Period %d:' %(j+1))
            for k in range(R):
                print('  Room %d:' %(k+1),a[4*i+j,k])
    print('=========')
    print('Total:',len(a)//4,'days')
solu=greedy()
t=[]
for i in solu:
    if np.any(i!=None):
        t.append(i)
if len(t)%4 !=0:
    t+=[[None]*R]*(4-len(t)%4)
t=np.array(t)
print_solu(t)

        