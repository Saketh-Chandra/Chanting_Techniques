def kramapatha(s):
    sm = list(map(str, s.split(" ")))
    x=[]
    gh = []
    l = len(sm)
    k = l
    for i in range(l):

        if (i == k - 1):
            gh.append(sm[l - 1])
            gh.append(sm[l - 1])
        else:
            gh.append(sm[(i) % l])
            gh.append(sm[(i + 1) % l])
    x.append(list(gh))
    return x
