def xpto(v, n):
    s = 0
    i = 0
    while i < n:
        if v[i] % 3 == 0:
            s = s + v[i]
        i = i + 1
    return s

A = [23, 4, 21, 3, 23]
m1 = xpto(A, 5)

# R: [23,4,21,3,23]; sim ocorre passagem por referência