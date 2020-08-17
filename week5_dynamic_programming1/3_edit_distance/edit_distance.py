# Uses python3
def edit_distance(s, t):
    # write your code here
    T = [[None]*(len(t)+1) for i in range(0, len(s)+1)]
    c = len(s) + 1
    for i in range(0, c):
        T[i][0] = i
    r = len(t) + 1
    for i in range(0, r):
        T[0][i] = i

    for i in range(1, c):
        for j in range(1, r):

            # for x in T:
            #     print(x)
            insertion = T[i-1][j] + 1
            deletion = T[i][j-1] + 1
            match = T[i-1][j-1]
            if t[j-1] != s[i-1]:
                match += 1
            T[i][j] = min(insertion, deletion, match)

    # for x in T:
    #     print(x)
    return T[c-1][r-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
