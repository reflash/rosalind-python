def dead_pairs(s, i, m):
    if i < m:
        return 0
    elif i == m:
        return 1
    else:
        return s[i - (m + 1)]

def rabbit_pairs(n, m):
    s = list([1,1])
    for i in range(2,n):
        s.append(s[i - 1] + s[i - 2] - dead_pairs(s, i, m))
    return s[-1]
