from ortools.sat.python import cp_model
import numpy as np
import time
# INPUT:
def input(filename):
    global N, student, M, c, conflict
    with open(filename) as f:
        N = int(f.readline())
        student = np.array(f.readline().split(), dtype=int)
        M = int(f.readline())
        c = np.array(f.readline().split(), dtype=int)
        t = int(f.readline())
        conflict = np.array([[int(num) for num in line.split()] for line in f])
input('data25.txt')
print(N)
print(student)
print(M)
print(c)
print(conflict)
K = 4
X = {}
y = {}
model = cp_model.CpModel()
solver = cp_model.CpSolver()
for k in range(N):
    for i in range(M):
        for j in range(N):
            X[k, i, j] = model.NewIntVar(0, 1, 'X['+str(k)+','+str(i)+','+str(j)+']')

# 1st constraint: each class contains no more than 1 test in 1 period in a day
print('Processing ....')
for k in range(N):
    for i in range(M):
        model.Add(sum(X[k, i, j] for j in range(N)) <= 1)

# 2nd constraint: each subject is tested exactly once
for j in range(N):
    model.Add(sum(X[k, i, j] for k in range(N) for i in range(M)) == 1)

# 3rd constraint: a class can not contain more students than its capacity
for k in range(N):
    for i in range(M):
        model.Add(sum(student[j]*X[k, i, j] for j in range(N)) <= c[i])

# 4th constraint: two conflicting subjects can not be tested in a period in 1 day
for k in range(N):
    for con in conflict:
        for i1 in range(M):
            for i2 in range(M):
                if i1 != i2:
                    model.Add(X[k, i1, con[0] - 1] + X[k, i2, con[1] - 1] <= 1)
for d in range(N//K+1):
    y[d] = model.NewIntVar(0, 1, 'y['+str(d)+']')
for k in range(N):
    model.Add(sum(X[k, i, j] for i in range(M) for j in range(N)) - M*y[k//K] <= 0)
start = time.time()
# Objective function:
model.Minimize(sum(d*y[d] for d in range(N//K+1)))


status = solver.Solve(model)
days = np.zeros(N//K+1, dtype=int)
if status == cp_model.OPTIMAL:
    for d in range(N//K+1):
        days[d] = solver.Value(y[d])
    for k in range(N):
        for i in range(M):
            for j in range(N):
                X[k, i, j] = solver.Value(X[k, i, j])
    print('the minimum test days is: ', int(sum(days)))
print('Processing ....')
end = time.time()
# Print the output
for d in range(N//4):
    if days[d] == 1:
        print('*** DAY ', d+1 ,'***')
        for k in range(4*d, 4*d+4):
            print('-period ', k%4+1,':')
            for i in range(M):
                for j in range(N):
                    if X[k, i, j] == 1:
                        print('    Room', i+1, ' :subject: ', j+1)

print('Running time: %.4f s '%( end - start))