# # Uses python3
# import sys
# import math


# def dist(p1, p2):
#     return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


# def y_sort(e):
#     return e[1]


# def minimum_distance(points, left, right):
#     # write your code here
#     if left == right:
#         return 2**31
#     mid = (left+right+1)//2
#     d1 = minimum_distance(points, left, mid)
#     d2 = minimum_distance(points, mid, right)
#     d = min(d1, d2)
#     new_points = [i for i in points if abs(i[0]-points[mid][0]) <= d]
#     new_points.sort(key=y_sort)
#     d_ = 2**31
#     for i in range(0, len(new_points)):
#         for j in range(i+1, len(new_points)):
#             if abs(new_points[i][1] - new_points[j][1]) > d:
#                 continue
#             new_dist = dist(new_points[i], new_points[j])
#             if new_dist < d_:
#                 d_ = new_dist
#     d = min(d, d_)

#     return d


# if __name__ == '__main__':
#     # input = sys.stdin.read()
#     # data = list(map(int, input.split()))
#     # n = data[0]
#     # x = data[1::2]
#     # y = data[2::2]
#     n = int(input())
#     points = []
#     for i in range(0, n):
#         x, y = map(int, input().split())
#         points.append((x, y))
#     points.sort()
#     print("{0:.9f}".format(minimum_distance(points, 0, n-1)))

import math


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def closest_split_pair(p_x, p_y, delta, best_pair):
    ln_x = len(p_x)
    mx_x = p_x[ln_x // 2][0]

    s_y = [x for x in p_y if mx_x - delta <= x[0] <= mx_x + delta]

    best = delta
    ln_y = len(s_y)
    for i in range(ln_y - 1):
        for j in range(i+1, min(i + 5, ln_y)):
            p, q = s_y[i], s_y[j]
            dst = dist(p, q)
            if dst < best:
                best_pair = p, q
                best = dst
    return best_pair[0], best_pair[1], best


def brute(ax):
    mi = dist(ax[0], ax[1])
    p1 = ax[0]
    p2 = ax[1]
    ln_ax = len(ax)
    if ln_ax == 2:
        return p1, p2, mi
    for i in range(ln_ax-1):
        for j in range(i + 1, ln_ax):
            if i != 0 and j != 1:
                d = dist(ax[i], ax[j])
                if d < mi:
                    mi = d
                    p1, p2 = ax[i], ax[j]
    return p1, p2, mi


def closest_pair(ax, ay):
    ln_ax = len(ax)
    if ln_ax <= 3:
        return brute(ax)
    mid = ln_ax // 2
    Qx = ax[:mid]
    Rx = ax[mid:]

    midpoint = ax[mid][0]
    Qy = list()
    Ry = list()
    for x in ay:
        if x[0] < midpoint:
            Qy.append(x)
        else:
            Ry.append(x)

    (p1, q1, mi1) = closest_pair(Qx, Qy)
    (p2, q2, mi2) = closest_pair(Rx, Ry)

    if mi1 <= mi2:
        d = mi1
        mn = (p1, q1)
    else:
        d = mi2
        mn = (p2, q2)

    (p3, q3, mi3) = closest_split_pair(ax, ay, d, mn)

    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p3, q3, mi3


def solution(a):
    ax = sorted(a, key=lambda x: x[0])
    ay = sorted(a, key=lambda x: (x[1], x[0]))
    p1, p2, mi = closest_pair(ax, ay)
    return mi


# Input

if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # x = data[1::2]
    # y = data[2::2]
    n = int(input())
    points = []
    for i in range(0, n):
        x, y = map(int, input().split())
        points.append((x, y))
    points.sort()
    print("{0:.4f}".format(solution(points)))
