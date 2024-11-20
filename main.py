import numpy as np

def f(x):
    return np.exp(-x)

def bisect(inp, out, i):
    l = len(out) - 1
    if out[i] < inp[i]:
        for j in range(l):
            if out[l - j] > inp[l - j]:
                return inp[l - j]
    else:
        for j in range(l):
            if out[l - j] < inp[l - j]:
                return inp[l - j]

    return 0

n = 100

inp = [0.0, 1.0]
out = [f(inp[0]), f(inp[1])]

for i in range(1, n):
    old_inp = bisect(inp, out, i)
    current_inp = inp[i]

    new_inp = (old_inp + current_inp) / float(2.0)

    inp.append(new_inp)
    out.append(f(new_inp))

print("Expected: 0.567143290409783872999968662")
print("Found:   ", round(new_inp, 17))
