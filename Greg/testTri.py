arrayToTri = [0, 20, -34, 32, -212, 23]


def trie(listeTri: list):
    for i in range(len(listeTri)):
        index = i

        min = listeTri[i]

        for k in range(i, len(listeTri)):
            if listeTri[k] < min:
                min = listeTri[k]
                index = k

        temp = listeTri[i]
        listeTri[i] = listeTri[index]
        listeTri[index] = temp


trie(arrayToTri)
# print(arrayToTri)


def triSelection(tab: list) -> None:
    i: int
    j: int
    imin: int
    for i in range(0, len(tab) - 1):
        imin = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[imin]:
                imin = j
        if imin != i:
            tmp = tab[i]
            tab[i] = tab[imin]
            tab[imin] = tmp


triSelection(arrayToTri)
print(arrayToTri)
