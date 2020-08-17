# Uses python3

import sys
import numpy


def lcs2(a, b):
    # write your code here
    m = len(a)
    n = len(b)

    L = [[None]*(n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif a[i-1] == b[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    i, j = m, n
    sequence = []
    # for k in L:
    #     print(k)
    while L[i][j] != 0:
        if (i > 0 and j > 0) and a[i-1] == b[j-1]:
            sequence.append(a[i-1])
            i -= 1
            j -= 1
        elif i > 0 and L[i-1][j] == L[i][j]:
            i = i-1
        elif j > 0 and L[i][j-1] == L[i][j]:
            j = j - 1
    return L[m][n], sequence[::-1]


def lcs3(a, b, c):
    # write your code here
    # count1, seq1 = lcs2(a, b)
    # for i in seq1:
    #     if i not in c:
    #         return 0
    # count2, seq2 = lcs2(b, c)
    # for i in seq2:
    #     if i not in a:
    #         return 0
    # count3, seq3 = lcs2(c, a)
    # for i in seq3:
    #     if i not in b:
    #         return 0
    # count = min(count1, count2, count3)
    # # count1, seq = lcs2(seq1, seq2)
    # # count2, seq = lcs2(seq2, seq3)
    # # count3, seq = lcs2(seq3, seq1)
    # return count
    Matrix = numpy.zeros((len(a)+1, len(b)+1, len(c)+1))

    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            for k in range(1, len(c)+1):
                if a[i-1] == b[j-1] == c[k-1]:
                    Matrix[i][j][k] = Matrix[i-1][j-1][k-1] + 1
                else:
                    Matrix[i][j][k] = max(
                        Matrix[i-1][j][k], Matrix[i][j-1][k], Matrix[i][j][k-1])

    return int(Matrix[-1][-1][-1])


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # an = data[0]
    # data = data[1:]
    # a = data[:an]
    # data = data[an:]
    # bn = data[0]
    # data = data[1:]
    # b = data[:bn]
    # data = data[bn:]
    # cn = data[0]
    # data = data[1:]
    # c = data[:cn]
    n = int(input())
    a = [int(i) for i in input().split()]
    assert n == len(a)
    m = int(input())
    b = [int(i) for i in input().split()]
    assert m == len(b)
    l = int(input())
    c = [int(i) for i in input().split()]
    assert l == len(c)
    print(lcs3(a, b, c))
