L = [10, 4, 6, 8, 3, 4, 5, 7, 7]
n = 4

def getSublists(L,n):
    sublist = []
    for i in range(len(L)-n+1):
        sublist.append(L[i:i+n])
    return sublist
print(getSublists(L,n))