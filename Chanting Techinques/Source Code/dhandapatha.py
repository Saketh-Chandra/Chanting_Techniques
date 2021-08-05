def dhandapatha(s):
    sm = list(map(str, s.split(" ")))
    l = len(sm)
    x=[]
    for i in range(4):
        gh = []
        if (i == 0):
            gh.append(sm[i])
            gh.append(sm[i + 1])

            gh.append(sm[i + 1])
            gh.append(sm[i])

            gh.append(sm[i])
            gh.append(sm[i + 1])
            gh.append(sm[i+2])

            gh.append(sm[i+2])
            gh.append(sm[i + 1])
            gh.append(sm[i])

            x.append(gh)
        elif (i == 1):
            gh.append(sm[i - 1])
            gh.append(sm[i])

            gh.append(sm[i])
            gh.append(sm[i + 1])

            gh.append(sm[i + 1])
            gh.append(sm[i + 2])

            gh.append(sm[i + 2])
            gh.append(sm[i + 1])
            gh.append(sm[i])
            gh.append(sm[i - 1])

            gh.append(sm[i - 1])
            gh.append(sm[i])

            gh.append(sm[i])
            gh.append(sm[i + 1])

            x.append(gh)

        elif (i == 2):
            gh.append(sm[i])
            gh.append(sm[i + 1])
            gh.append(sm[i + 1])
            gh.append(sm[i + 2])

            gh.append(sm[i + 2])
            gh.append(sm[i + 1])
            gh.append(sm[i])
            gh.append(sm[i - 1])
            gh.append(sm[i - 2])

            x.append(gh)

        elif (i == 3):
            gh.append(sm[i - 3])
            gh.append(sm[i - 2])

            gh.append(sm[i - 2])
            gh.append(sm[i - 1])

            gh.append(sm[i - 1])
            gh.append(sm[i])

            gh.append(sm[i])
            gh.append(sm[i + 1])

            gh.append(sm[i + 1])
            gh.append(sm[i + 2])

            gh.append(sm[i + 2])
            gh.append(sm[i + 1])
            gh.append(sm[i])
            gh.append(sm[i-1])
            gh.append(sm[i - 2])
            gh.append(sm[i - 3])
            x.append(gh)
    return x



