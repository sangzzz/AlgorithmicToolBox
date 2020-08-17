# Uses python3
import sys


def get_change(m):
    # write your code here
    i = m
    x = i//10 + (i % 10)//5 + ((i % 10) % 5)
    return x


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
