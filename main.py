import numpy as np

# starting interval
x1 = 0.0
x2 = 1.0

n_iterations = 100

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

inp = [x1, x2]
out = [f(inp[0]), f(inp[1])]

for i in range(n_iterations):
    old_inp = bisect(inp, out, i)
    current_inp = inp[i]

    new_inp = (old_inp + current_inp) / float(2.0)

    inp.append(new_inp)
    out.append(f(new_inp))

print("Expected: 0.567143290409783872999968662")
print("Found:   ", round(new_inp, 17))
