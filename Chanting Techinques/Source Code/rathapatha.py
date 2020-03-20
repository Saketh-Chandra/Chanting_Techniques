def rathapatha(s):
    sm = list(map(str, s.split(" ")))
    x = []
    i = 0
    for j in range(9):
        gh = []
        if j == (0):
            gh.append(sm[i])
            gh.append(sm[i + 1])

            gh.append(sm[i + 3])
            gh.append(sm[i + 4])

            x.append(gh)
        elif j == 1:
            gh.append(sm[i + 1])
            gh.append(sm[i])

            gh.append(sm[i + 4])
            gh.append(sm[i + 3])

            x.append(gh)

        elif j == 2:
            gh.append(sm[i])
            gh.append(sm[i + 1])

            gh.append(sm[i + 3])
            gh.append(sm[i + 4])

            x.append(gh)

        elif j == (3):
            gh.append(sm[i + 1])
            gh.append(sm[i + 2])

            gh.append(sm[i + 4])
            gh.append(sm[i + 5])

            x.append(gh)


        elif j == 4:
            gh.append(sm[i + 2])
            gh.append(sm[i + 1])
            gh.append(sm[i])

            x.append(gh)

        elif j == 5:
            gh.append(sm[i + 5])
            gh.append(sm[i + 4])

            gh.append(sm[i + 3])

            x.append(gh)

        elif j == 6:
            gh.append(sm[i])
            gh.append(sm[i + 1])

            gh.append(sm[i + 3])
            gh.append(sm[i + 4])

            x.append(gh)

        elif j == 7:
            gh.append(sm[i + 1])
            gh.append(sm[i + 2])

            gh.append(sm[i + 4])
            gh.append(sm[i + 5])

            x.append(gh)

        elif j == 8:
            gh.append(sm[i + 2])
            gh.append(sm[i + 2])

            gh.append(sm[i + 5])
            gh.append(sm[i + 5])

            x.append(gh)
    return x


