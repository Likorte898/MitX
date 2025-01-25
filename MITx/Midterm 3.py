def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''

    ans = []
    # for k, v in aDict.iteritems():
    for k, v in aDict.items():
        if v == target:
            ans.append(k)
    return sorted(ans)

