def malapatha(s):
    sm = list(map(str, s.split(" ")))
    gh = []
    l = len(sm)
    x = []
    n = l
    j = n - 1
    k = 0
    for i in range(n):
        gh = []
        while 1:
            if k == n - 1:
                gh.append(sm[k])
                gh.append(sm[k])

                break
            else:
                gh.append(sm[k])
                gh.append(sm[k + 1])
                k += 1
                break
        while 1:
            if j == n - 1:
                gh.append(sm[j])
                gh.append(sm[j])
                j -= 1
                break
            else:
                gh.append(sm[j + 1])
                gh.append(sm[j])
                j -= 1
                break
        x.append(gh)
    return x