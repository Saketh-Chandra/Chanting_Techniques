def rekhapatha(s):
    sm = list(map(str, s.split(" ")))
    l = len(sm)
    gh = []
    x = []
    for i in range(3):
        gh = []
        if i == 0:
            gh.append(sm[i])
            gh.append(sm[i + 1])

            gh.append('|')

            gh.append(sm[i + 1])
            gh.append(sm[i])

            gh.append('|')

            gh.append(sm[i])
            gh.append(sm[i + 1])

            gh.append('|')

            gh.append(sm[i + 1])
            gh.append(sm[i + 2])
            gh.append(sm[i + 3])

            gh.append('|')

            gh.append(sm[i + 3])
            gh.append(sm[i + 2])
            gh.append(sm[i + 1])

            gh.append('|')

            x.append(gh)


        elif i == 1:
            gh.append(sm[i])
            gh.append(sm[i + 1])

            gh.append('|')

            gh.append(sm[i + 1])
            gh.append(sm[i + 2])
            gh.append(sm[i + 3])
            gh.append(sm[i + 4])

            gh.append('|')

            gh.append(sm[i + 4])
            gh.append(sm[i + 3])
            gh.append(sm[i + 2])
            gh.append(sm[i + 1])

            gh.append('|')

            x.append(gh)



        elif i == 2:
            gh.append(sm[i])
            gh.append(sm[i + 1])

            gh.append('|')

            gh.append(sm[i + 1])
            gh.append(sm[i + 2])

            gh.append('|')

            gh.append(sm[i + 2])
            gh.append(sm[i + 3])

            gh.append('|')

            gh.append(sm[i + 3])
            gh.append(sm[i + 3])

            gh.append('|')

            x.append(gh)



    return x
