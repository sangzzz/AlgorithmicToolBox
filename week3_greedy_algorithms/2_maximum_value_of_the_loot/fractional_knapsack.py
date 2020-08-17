# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0
    W = capacity
    # write your code here
    # print(capacity, weights, values)
    while W > 0:
        max_value = -1
        index = len(weights)
        for i in range(0, len(weights)):
            if weights[i] != 0 and values[i]/weights[i] > max_value:
                max_value = values[i]/weights[i]
                index = i
        if index == len(weights):
            break
        w = min(W, weights[index])
        value = value + (w * values[index] / weights[index])
        weights[index] = weights[index] - w
        W = W - w
    return value


if __name__ == "__main__":
    n, capacity = map(int, input().split())
    values = []
    weights = []
    for i in range(0, n):
        x, y = map(int, input().split())
        values.append(x)
        weights.append(y)
    # values = data[2:(2 * n + 2):2]
    # weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
