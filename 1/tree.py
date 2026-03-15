import sys

def main():
    P, V = map(int, input().split())
    Q, M = map(int, input().split())
    L1, R1 = P-V, P+V
    L2, R2 = Q-M, Q+M
    A = abs((P+V) - (P-V)) + 1
    B = abs((Q+M) - (Q-M)) + 1
    U = max(0, min(R1, R2) - max(L1, L2) + 1) 
    result = A + B - U
    print(result)


if __name__ == '__main__':
    main()


