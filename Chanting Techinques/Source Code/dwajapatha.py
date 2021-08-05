def dwajapatha(s):

    sm = list(map(str, s.split(" ")))
    gh = []
    l = len(sm)
    x=[]
    n = l - 1
    for i in range(2):
        gh = []
        if i == 0:
            gh.append(sm[i])
            gh.append(sm[i + 1])
            gh.append("|")

            gh.append(sm[n])
            gh.append(sm[n])
            gh.append("|")

            gh.append(sm[i + 1])
            gh.append(sm[i + 2])
            gh.append("|")

            gh.append(sm[n])
            gh.append(sm[n - 1])
            gh.append("|")

            gh.append(sm[i + 2])
            gh.append(sm[i + 3])
            gh.append("|")

            gh.append(sm[n - 1])
            gh.append(sm[n - 2])

            x.append(gh)
        else:
            gh.append(sm[n - 2])
            gh.append(sm[n - 1])
            gh.append("|")

            gh.append(sm[n - 2])
            gh.append(sm[i + 1])
            gh.append("|")

            gh.append(sm[n - 1])
            gh.append(sm[n])
            gh.append("|")

            gh.append(sm[i + 1])
            gh.append(sm[i])
            gh.append("|")

            gh.append(sm[n])
            gh.append(sm[n])
            gh.append("|")

            gh.append(sm[i - 1])
            gh.append(sm[i])

            x.append(gh)

    return x