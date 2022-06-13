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
input('data10.txt')
print(N)
print(student)
print(R)
print(room)
print(a)
print(conflict)