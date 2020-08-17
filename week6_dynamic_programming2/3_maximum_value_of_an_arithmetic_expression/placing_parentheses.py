# Uses python3
import re


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(nums, ops):
    # write your code here
    m = []
    M = []
    for i in range(0, len(nums)):
        x = [None]*len(nums)
        m.append(x)
        x = [None]*len(nums)
        M.append(x)
    # M = [[None]*len(nums)]*len(nums)
    # m = [[None]*len(nums)]*len(nums)
    # m[0][0] = nums[0]
    # for i in range(0, len(nums)):
    #     for j in range(0, len(nums)):
    #         if i == j:
    #             m[i][i] = nums[i]
    #             M[i][i] = nums[i]
    # print(m, M)
    for i in range(0, len(nums)):
        m[i][i] = nums[i]
        M[i][i] = nums[i]

    def MinAndMax(i, j):
        m_ = 2**31
        M_ = -(2**31)
        for k in range(i, j):
            a = evalt(M[i][k], M[k+1][j], ops[k])
            b = evalt(M[i][k], m[k+1][j], ops[k])
            c = evalt(m[i][k], M[k+1][j], ops[k])
            d = evalt(m[i][k], m[k+1][j], ops[k])
            m_ = min(m_, a, b, c, d)
            M_ = max(M_, a, b, c, d)
        return m_, M_

    for s in range(1, len(nums)):
        for i in range(0, len(nums) - s):
            j = i+s
            m[i][j], M[i][j] = MinAndMax(i, j)
    # for i in m:
    #     print(i)
    # for i in M:
        # print(i)
    return M[0][-1]


if __name__ == "__main__":
    x = input()
    ops = [i for i in x if i in "+-*"]
    nums = []
    y = ""
    for i in x:
        if i not in ops:
            y += i
        else:
            nums.append(int(y))
            y = ''
    nums.append(int(y))
    # print(ops, nums[0])
    print(get_maximum_value(nums, ops))
