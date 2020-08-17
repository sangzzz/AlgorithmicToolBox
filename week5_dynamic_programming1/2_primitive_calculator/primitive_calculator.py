# Uses python3
import sys
import time
import math
import random


def opt_seq(n):
    T = {}
    # T[0] = 0
    T[1] = 0
    for i in range(2, n+1):
        possibleDerivations = []
        possibleDerivations.append(T[i-1])
        if i % 2 == 0:
            possibleDerivations.append(T[i//2])
        if i % 3 == 0:
            possibleDerivations.append(T[i//3])
        T[i] = min(possibleDerivations) + 1

    count = T[n]
    opt_sequence = [n]
    while n != 1:
        # possibleSequences = []
        # opt_sequence.append(n)
        x = T[n]
        if n % 3 == 0:
            # possibleSequences.append()
            if T[n//3] == T[n]-1:
                # opt_sequence.append(n//3)
                n = n // 3
                opt_sequence.append(n)
                continue
        elif n % 2 == 0:
            if T[n//2] == T[n]-1:
                n = n // 2
                opt_sequence.append(n)
                continue
        if T[n] == T[n-1]+1:
            # opt_sequence.append(n-1)
            n = n - 1
        opt_sequence.append(n)

    return count, opt_sequence[::-1]


# def optimal_sequence(n):
#     sequence = []
#     while n >= 1:
#         sequence.append(n)
#         if n % 3 == 0:
#             n = n // 3
#         elif n % 2 == 0:
#             n = n // 2
#         else:
#             n = n - 1
#     return reversed(sequence)

def test():
    while True:
        n = math.floor(random.random()*100000)+1
        print(opt_seq(n))
        time.sleep(5)


# input = sys.stdin.read()
# test()
n = int(input())
count, sequence = opt_seq(n)
print(count)
for x in sequence:
    print(x, end=' ')
