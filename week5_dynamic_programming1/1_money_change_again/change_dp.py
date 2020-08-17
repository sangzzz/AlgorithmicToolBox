# Uses python3
import sys


def get_change(m):
    # write your code here
    # Denominations are 1, 3, 4
    d = [1, 3, 4]
    T = {}
    T[0] = 0
    for i in range(1, m+1):
        T[i] = 2**31
        for j in d:
            if i - j >= 0:
                if T[i-j]+1 < T[i]:
                    T[i] = T[i-j] + 1

    return T[m]


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
