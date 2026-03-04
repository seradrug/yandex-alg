import sys

x = str(input())

def main(x):

    result = []
    i = len(x) - 1

    while i >= 0:
        if x[i] == '#':
            num = int(x[i-2:i])
            result.append(chr(96 + num))
            i -= 3
        else:
            num = int(x[i])
            result.append(chr(96 + num))
            i -= 1

    return "".join(reversed(result))

if __name__ == '__main__':
    print(main(x))

