
from challenge_input import codes


def go_basement(codes):
    base = 0
    for i in range(len(codes)):
        if codes[i] == '(':
            base += 1
        else:
            base -= 1
        if base == -1:
            return i + 1


if __name__ == '__main__':

    print go_basement(codes)
