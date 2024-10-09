# listeTrier = [0,15,648,22,3,48,7,7,451,156,-45,748,641,-4,564,-789]

# def fonctionTrie(laListe:list)->None:
#     i:int
#     l:list=[]
#     for i in len(listeTrier):
#         if i >i+1:
#             l.append(listeTrier[i+1]+listeTrier[i])
#         elif i>i+1:
#             l.append(listeTrier[i]+listeTrier[i+1])
#         else:
#             l.append(listeTrier[i]+listeTrier[i])
#     print (l)
# fonctionTrie(listeTrier)

def triSelection(tab:list)->None:
    i:int
    j:int
    imin:int
    for i in range(0,len(tab)-1):
        imin = i
    for j in range(i+1,len(tab)):
        if (tab[j]<tab[imin]):
            imin = j
        if(imin!=i):
            tmp = tab[i]
    tab[i] = tab[imin]
    tab[imin] = tmp
triSelection([5,2,15,2,158])