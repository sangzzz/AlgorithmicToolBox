# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    stops.append(distance)
    current = 0
    num = 0
    i = 1
    if distance <= tank:
        return 0
    while current != distance:
        previous = current
        while (stops[i] - previous) <= tank:
            current = stops[i]
            if current == distance:
                return num
            i = i + 1
        if current == previous:
            return -1
        num = num + 1


if __name__ == '__main__':
    distance = int(input())
    distance_full_tank = int(input())
    n = int(input())
    stops = list(map(int, input().split()))
    print(compute_min_refills(distance, distance_full_tank, [0] + stops))
