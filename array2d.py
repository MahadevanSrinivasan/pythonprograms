def performOps(A):
    m = len(A)
    n = len(A[0])
    B = []
    for i in xrange(len(A)):
        B.append([0] * n)
        for j in xrange(len(A[i])):
            B[i][n - 1 - j] = A[i][j]
    return B

A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
B = performOps(A)
for i in xrange(len(B)):
    for j in xrange(len(B[i])):
        print B[i][j],
