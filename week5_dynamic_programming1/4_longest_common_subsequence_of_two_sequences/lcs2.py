# Uses python3

import sys


def lcs2(a, b):
    # write your code here
    m = len(a)
    n = len(b)

    # declaring the array for storing the dp values
    L = [[None]*(n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif a[i-1] == b[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    # for i in L:
    #     print(i)
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
    # write your code here
    # T = [[None]*(len(b)+1) for i in range(0, len(a)+1)]
    # c = len(a) + 1
    # for i in range(0, c):
    #     T[i][0] = i
    # r = len(b) + 1
    # for i in range(0, r):
    #     T[0][i] = i

    # for i in range(1, c):
    #     for j in range(1, r):

    #         # for x in T:
    #         #     print(x)
    #         insertion = T[i-1][j] + 1
    #         deletion = T[i][j-1] + 1
    #         match = T[i-1][j-1]
    #         if b[j-1] != a[i-1]:
    #             match += 1
    #         T[i][j] = min(insertion, deletion, match)

    # for x in T:
    #     print(x)
    # i = c-1
    # j = r-1
    # count = 0
    # while not (i==0 and j==0):
    #     val = T[i][j]
    #     moves = []
    #     if i!=0:
    #         up = T[i-1][j]
    #         moves.append(up)
    #     if j!=0:
    #         left = T[i][j-1]
    #         moves.append(down)
    #     if i!=0 and j!=0:
    #         diag = T[i-1][j-1]
    #     move = min([up, left, diag])
    #     if diag == move:
    #         i -= 1
    #         j -= 1
    #     elif up == move:
    #         i -= 1
    #     elif left == move:
    #         j -= 1

    # return count

    # return min(len(a), len(b))


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))

    # n = data[0]
    # data = data[1:]
    # a = data[:n]

    # data = data[n:]
    # m = data[0]
    # data = data[1:]
    # b = data[:m]

    n = int(input())
    a = [int(i) for i in input().split()]
    assert n == len(a)

    m = int(input())
    b = [int(i) for i in input().split()]
    assert m == len(b)

    print(lcs2(a, b))
