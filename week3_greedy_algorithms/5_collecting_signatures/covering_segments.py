# Uses python3
import sys


def check(x):
    for i in x:
        if i == 0:
            return 1
    return 0


def find_min(b, x):
    i = 0
    min_stop = 2**31
    index = len(b)
    while i < len(b):
        if b[i] < min_stop and x[i] == 0:
            min_stop = b[i]
            index = i
        i = i + 1
    return index


def optimal_points(a, b):
    points = []
    # write your code here
    x = [0 for i in a]
    points = []
    while check(x) == 1:
        stop_index = find_min(b, x)
        stop = b[stop_index]
        i = 0
        while i < len(a):
            if a[i] <= stop and b[i] >= stop:
                x[i] = 1
            i = i+1
        points.append(stop)
    return len(points), points


if __name__ == '__main__':
    n = int(input())
    a = []
    b = []
    for i in range(n):
        start, end = map(int, input().split())
        a.append(start)
        b.append(end)
    number, points = optimal_points(a, b)
    output_points = ""
    for i in points:
        output_points = output_points + str(i) + ' '
    print(number)
    print(output_points)
