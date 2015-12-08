
import collections


# part I rules

def nice_I(line):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return map(lambda x: x in vowels, line).count(True) >= 3


def nice_II(line):
    result = False
    d = collections.defaultdict(int)
    for i in range(len(line)):
        if line[i] in d.keys() and line[i-1] == line[i]:
            return True
        else:
            d[line[i]] += 1
    return result


def nice_III(line):
    nice = True
    bad_substrings = ['ab', 'cd', 'pq', 'xy']
    for b in bad_substrings:
        if line.find(b) >= 0:
            return False
    return nice


# part II rules

def nice_IV(line):
    result = False
    for i in range(len(line)-2):
        p = line[i:i+2]
        if line[i+2:].find(p) >= 0:
            return True
    return result


def nice_V(line):

    result = False
    for i in range(len(line) - 3):
        if line[i] == line[i+2]:
            return True
    return result


def p_1(line):
    return nice_III(line) and nice_II(line) and nice_I(line)


def p_2(line):
    return nice_IV(line) and nice_V(line)


if __name__ == '__main__':
    with open('./input.txt', 'r') as fd:
        input_lines = fd.readlines()

    sol = 0
    for line in input_lines:
        if p_2(line):
            sol += 1
    print sol
