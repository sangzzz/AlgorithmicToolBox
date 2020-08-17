# Uses python3
import sys
import itertools


def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


T = {}


def partition(A, sumlist):
    x = A[0]
    a = sumlist[0] - x
    b = sumlist[1] - x
    c = sumlist[2] - x
    if sumlist in T:
        return T[sumlist]
    T[sumlist] = False
    if a >= 0 and len(A) > 1:
        y = (min(a, sumlist[1], sumlist[2]), sum((a, sumlist[1], sumlist[2])) - max(a, sumlist[1],
                                                                                    sumlist[2]) - min(a, sumlist[1], sumlist[2]), max((a, sumlist[1], sumlist[2])))
        T[sumlist] = T[sumlist] or partition(A[1:], y)
    if b >= 0 and len(A) > 1:
        y = (min(b, sumlist[0], sumlist[2]), sum((b, sumlist[0], sumlist[2])) - max(b, sumlist[0],
                                                                                    sumlist[2]) - min(b, sumlist[0], sumlist[2]), max((b, sumlist[0], sumlist[2])))
        T[sumlist] = T[sumlist] or partition(A[1:], y)
    if c >= 0 and len(A) > 1:
        y = (min(c, sumlist[0], sumlist[1]), sum((c, sumlist[0], sumlist[1])) - max(c, sumlist[0],
                                                                                    sumlist[1]) - min(c, sumlist[0], sumlist[1]), max((c, sumlist[0], sumlist[1])))
        T[sumlist] = T[sumlist] or partition(A[1:], y)
    if (a == 0 and sumlist[1] == 0 and sumlist[2] == 0) or (b == 0 and sumlist[0] == 0 and sumlist[2] == 0) or (c == 0 and sumlist[1] == 0 and sumlist[0] == 0):
        T[sumlist] = True
    return T[sumlist]


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *A = list(map(int, input.split()))
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    x = sum(A)
    if x % 3 != 0:
        print(0)
        sys.exit()
    sumlist = (x//3, x//3, x//3)
    T[(0, 0, 0)] = True
    if partition(A, sumlist):
        print(1)
    else:
        print(0)
    # print(T)
    # print(partition(A, sumlist))


def partitions(W, n, items):
    """ Finds if number of partitions having capacity W is >=3
    (int, int, list) -> (int) """
    count = 0
    value = numpy.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
            value[i][j] = value[i][j-1]
            if items[j-1] <= i:
                temp = value[i-items[j-1]][j-1] + items[j-1]
                if temp > value[i][j]:
                    value[i][j] = temp
            if value[i][j] == W:
                count += 1

    if count < 3:
        print('0')
    else:
        print('1')
