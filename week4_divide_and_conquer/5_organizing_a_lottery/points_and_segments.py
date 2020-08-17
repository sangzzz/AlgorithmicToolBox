# Uses python3
import sys
import math
import random


# def fast_count_segments(starts, ends, points):
#     cnt = [0] * len(points)
#     segments = []
#     for i in range(0, len(starts)):
#         segments.append((starts[i], ends[i]))
#     segments.sort()
#     # print(segments[0])
#     for i in range(0, len(points)):
#         p = points[i]
#         left = 0
#         right = len(starts)-1
#         mid = (left+right)//2
#         if segments[0][0] > p:
#             cnt[i] = 0
#             continue
#         # elif segments[-1][0] <= p:
#         #     for k in range(0, right+1):
#         #         if segments[k][1] >= p >= segments[k][0]:
#         #             cnt[i] += 1
#         #     continue
#         j = len(segments)
#         while True:
#             mid = (left+right)//2
#             if right > left:
#                 if segments[mid][0] == p:
#                     if mid != len(segments):
#                         if segments[mid+1][0] > p:
#                             j = mid
#                             break
#                         else:
#                             left = mid + 1
#                             continue
#                 elif segments[mid][0] > p:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             else:
#                 j = mid
#                 break
#         for k in range(0, j+1):
#             if segments[k][1] >= p >= segments[k][0]:
#                 cnt[i] += 1
#         # print(cnt)

#         # write your code here
#     return cnt

# Above fn, i have tried to get the lowest start point which is larger than the req point, for each point.
# Using biary search logic. Worst case complexity is same as naive algorithm.
# But at average case, it works in O(p*logn + nlogn)

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    all_points = []
    for i in starts:
        all_points.append((i, 0))
    for i in points:
        all_points.append((i, 1))
    for i in ends:
        all_points.append((i, 2))

    all_points.sort()  # O((2n + p) * log(2n + p))

    segments = 0
    point_count = {}

    for i in all_points:
        if i[1] == 0:
            segments += 1
        elif i[1] == 2:
            segments -= 1
        else:
            point_count[i[0]] = segments
    # O(2n + p)

    for i in range(0, len(points)):
        cnt[i] = point_count[points[i]]
    # O(p)

    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


def stress_test():
    while True:
        n = math.floor(random.random() * 1000) + 1
        starts = []
        ends = []
        points = []
        for i in range(0, n):
            s1 = math.floor(random.random()*10)-5
            s2 = math.floor(random.random()*10)-5
            starts.append(min(s1, s2))
            ends.append(max(s1, s2))
        p = math.floor(random.random() * 1000)+10
        for i in range(0, p):
            points.append(math.floor(random.random() * 10 - 5))

        cnt1 = naive_count_segments(starts, ends, points)
        cnt2 = fast_count_segments(starts, ends, points)
        if cnt1 == cnt2:
            print("Success!")
        else:
            print(starts)
            print(ends)
            print(points)
            print("Naive: ", cnt1)
            print("Fast : ", cnt2)
            break


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # m = data[1]
    # starts = data[2:2 * n + 2:2]
    # ends = data[3:2 * n + 2:2]
    # points = data[2 * n + 2:]
    # # use fast_count_segments
    # inp = input().split()
    # s = int(inp[0])
    # p = int(inp[1])
    # stress_test()
    s, p = map(int, input().split())
    starts = []
    ends = []
    for i in range(0, s):
        s1, s2 = map(int, input().split())
        starts.append(s1)
        ends.append(s2)
    points = list(map(int, input().split()))
    assert p == len(points)
    # cnt = naive_count_segments(starts, ends, points)
    # for x in cnt:
    #     print(x, end=' ')
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
