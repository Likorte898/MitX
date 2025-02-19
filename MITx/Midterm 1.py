def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    n = 1
    while True:
        if b**n == x:
            return n
        elif b**n > x:
            return (n-1)
        else:
            n += 1

print(myLog(16,2))