def jathapatha(s):
    sm = list(map(str, s.split(" ")))
    gh = []
    l = len(sm)
    x=[]
    k = l - 1

    for i in range(l - 1):
        gh = []
        if (i == k - 1):
            gh.append(sm[(i) % l])
            gh.append(sm[(i + 1) % l])

            gh.append(sm[(i + 1) % l])
            gh.append(sm[i % l])

            gh.append(sm[i % l])
            gh.append(sm[(i + 1) % l])

            gh.append(sm[k])
            gh.append(sm[k])
        else:
            gh.append(sm[(i) % l])
            gh.append(sm[(i + 1) % l])

            gh.append(sm[(i + 1) % l])
            gh.append(sm[i % l])

            gh.append(sm[i % l])
            gh.append(sm[(i + 1) % l])
        x.append(gh)
    return x