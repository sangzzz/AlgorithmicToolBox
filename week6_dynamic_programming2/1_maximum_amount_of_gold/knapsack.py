# Uses python3
import sys


def optimal_weight(W, w):
    # write your code here
    result = 0

    for x in w:
        if result + x <= W:
            result = result + x
    return result


def opt_weight(W, w, T):
    # print(w)
    for i in range(0, len(w)):
        for j in range(1, W+1):
            T[j][i+1] = T[j][i]
            if w[i] <= j:
                T[j][i+1] = max(T[j][i+1], T[j][i], T[j-w[i]][i] + w[i])
    # print(T)
    # for x in T:
    #     print(x)
    return T[-1][-1]


if __name__ == '__main__':
    # input = sys.stdin.read()
    # W, n, *w = list(map(int, input.split()))
    W, n = map(int, input().split())
    w = [int(i) for i in input().split()]
    T = [[0]*(len(w)+1) for i in range(0, W+1)]
    print(opt_weight(W, w, T))
