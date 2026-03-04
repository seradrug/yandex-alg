import sys

def solve():
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(1)
        return

    # prefix sums S[k] = sum of a[0..k-1]
    S = [0] * (n + 1)
    for i in range(n):
        S[i + 1] = S[i] + a[i]

    # cond[j]: can sum of first (j+1) elements absorb a[j+1]?
    cond = [False] * (n - 1)
    for j in range(n - 1):
        cond[j] = (S[j + 1] > a[j + 1])

    # good[i]: all cond[j] for j in [i..n-2] are True
    good = [False] * n
    good[n - 1] = True
    for i in range(n - 2, -1, -1):
        good[i] = cond[i] and good[i + 1]

    mn = a[0]
    out = []
    for i in range(n):
        can_win = good[i] and (a[i] > mn)
        out.append("1" if can_win else "0")

    print("\n".join(out))

if __name__ == "__main__":
    solve()
