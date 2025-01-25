def flatten(aList):

    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''

    newList = []
    for item in aList:
        if type(item) != type([]):
            newList.append(item)
        else:
            newList.extend(flatten(item))
    return newList

L = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(L))

