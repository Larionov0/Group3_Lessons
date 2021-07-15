def n_spis(n):
    n_s = []
    n_index = 1
    while n_index <= n:
        n_s.append(n)
        n_index += 1
    return n_s


spis = n_spis(3)
print(spis)
