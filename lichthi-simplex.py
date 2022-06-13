import  numpy as np
from ortools.linear_solver import pywraplp
import time
def input(filename):
    global N,d,M,c,conflict
    with open(filename) as f:
        N = int(f.readline())
        d = np.array(f.readline().split(),dtype=int)
        M = int(f.readline())
        c = np.array(f.readline().split(),dtype=int)
        t = int(f.readline())
        conflict = np.array([[int(num) for num in line.split()] for line in f])
input('data200.txt')
print('N= ', N)
print('d= ',d)
print('M = ',M)
print('c = ',c)
print('conflict = ',conflict)
print('Processing .....')
X = {}
solver = pywraplp.Solver.CreateSolver('b','CBC')
for k in range(N):
    for i in range(M):
        for j in range(N):
            X[k,i,j] = solver.IntVar(0,1,'X['+str(k)+','+str(i)+','+str(j)+']')
y = {}
for k in range(N//4+1):
    y[k] = solver.IntVar(0,1,'y['+str(k)+']')
# Moi mon thi 1 lan
for j in range(N):
    solver.Add(sum(X[k,i,j] for k in range(N) for i in range(M)) == 1)
# So hoc sinh < so cho ngoi
for k in range(N):
    for i in range(M):
        solver.Add(sum(X[k,i,j]*d[j] for j in range(N)) <= c[i])
# 1 phong thi 1 mon
for k in range(N):
    for i in range(M):
        solver.Add(sum(X[k,i,j] for j in range(N)) <= 1)
# 2 mon conflict ko thi cung nhau
for k in range(N):
    for con in conflict:
        c = solver.Constraint(0,1)
        for i in range(M):
            c.SetCoefficient(X[k,i,con[0]-1],1)
            c.SetCoefficient(X[k,i,con[1]-1],1)
for k in range(N):
    solver.Add(sum(X[k,i,j] for i in range(M) for j in range(N)) <= M*y[k // 4])

start = time.time()
# Objective
solver.Minimize(solver.Sum(k*y[k] for k in range(N//4+1)))
result_status = solver.Solve()
assert result_status == pywraplp.Solver.OPTIMAL

day = N//4
end = time.time()
for d in range(day):
    if y[d].solution_value() == 1:
        print('*** DAY ',d+1,'***')
        for k in range(4*d, 4*(d+1)):
                print('- Period ', k%4 +1,':')
                for i in range(M):
                    for j in range(N):
                        if X[k,i,j].solution_value() == 1:
                            print('   Room',i+1,' :subject%5d'%(j+1))
print('==========')
print('Optimal object value = %f' % sum([y[k].solution_value() for k in range(N//4+1)]))
print('Running time: %.4f s '%(end - start) )

