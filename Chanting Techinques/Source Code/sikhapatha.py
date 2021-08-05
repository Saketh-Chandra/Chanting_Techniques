def sikhapatha(s):
    sm = list(map(str, s.split(" ")))
    gh = []
    l = len(sm)
    x = []
    k = l - 1

    for i in range(l):
        gh = []
        if (i == k):
            gh.append(sm[k])
            gh.append(sm[k])
        elif (i == k - 1):
            gh.append(sm[(i) % l])
            gh.append(sm[(i + 1) % l])

            gh.append(sm[(i + 1) % l])
            gh.append(sm[i % l])

            gh.append(sm[(i) % l])
            gh.append(sm[(i + 1) % l])
        else:
            gh.append(sm[(i) % l])
            gh.append(sm[(i + 1) % l])

            gh.append(sm[(i + 1) % l])
            gh.append(sm[i % l])

            gh.append(sm[i % l])
            gh.append(sm[(i + 1) % l])
            gh.append(sm[(i + 2) % l])

        x.append(gh)
    return x
