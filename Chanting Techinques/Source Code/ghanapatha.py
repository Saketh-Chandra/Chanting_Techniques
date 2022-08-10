def ghanapatha(s):
    sm = list(map(str, s.split(" ")))
    gh = []
    l = len(sm)
    x=[]
    k = l - 1

    for i in range(l):
        gh = []
        if i == k - 1:
            continue
        if (i == k):
            gh.append(sm[k])
            gh.append(sm[k])
        else:
            gh.append(sm[(i) % l])
            gh.append(sm[(i + 1) % l])

            gh.append(sm[(i + 1) % l])
            gh.append(sm[i % l])

            gh.append(sm[i % l])
            gh.append(sm[(i + 1) % l])
            gh.append(sm[(i + 2) % l])

            gh.append(sm[(i + 2) % l])
            gh.append(sm[(i + 1) % l])
            gh.append(sm[i % l])

            gh.append(sm[i % l])
            gh.append(sm[(i + 1) % l])
            gh.append(sm[(i + 2) % l])
        x.append(gh)
    return x



























""""
s=str(input("enter the lines: "))

sm=list(map(str,s.split(" ")))
ghanapatha=[]
l=len(sm)
#print(sm)
k=l-1
#print(k)
for i in range(l):
    ghanapatha=[]
    if i==k-1:
        continue
    if (i==k):
        ghanapatha.append(sm[k])
        ghanapatha.append(sm[k])
    else:
        ghanapatha.append(sm[(i) % l])
        ghanapatha.append(sm[(i + 1) % l])

        ghanapatha.append(sm[(i + 1) % l])
        ghanapatha.append(sm[i % l])

        ghanapatha.append(sm[i % l])
        ghanapatha.append(sm[(i + 1) % l])
        ghanapatha.append(sm[(i + 2) % l])

        ghanapatha.append(sm[(i + 2) % l])
        ghanapatha.append(sm[(i + 1) % l])
        ghanapatha.append(sm[i % l])

        ghanapatha.append(sm[i % l])
        ghanapatha.append(sm[(i + 1) % l])
        ghanapatha.append(sm[(i + 2) % l])
    li = " ".join(ghanapatha)
    print(li)
"""