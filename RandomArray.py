import random

u = [random.randint(-15, 15) for _ in range(5)]
v = [random.randint(-15, 15) for _ in range(5)]
u,v

w = [None] * 5
for i in range(5):
    u[i] = 3*u[i]
    v[i] = 2*v[i]
    u[i],v[i]
    w[i] = u[i]-v[i]

w
