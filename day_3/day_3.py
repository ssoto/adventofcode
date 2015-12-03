
from challenge_input import input


def get(pos, x, y):
    pos = pos.split(',')
    c_x = int(pos[0]) + x
    c_y = int(pos[1]) + y
    return '{},{}'.format(c_x, c_y)


def houses_of(line):
    result = ['0,0']
    p_santa = p_robot = '0,0'

    for i in range(len(line)):

        if i % 2 == 0:
            p = p_santa
        else:
            p = p_robot

        char = line[i]
        if char == '^':
            element = get(p, +1, 0)
        elif char == 'v':
            element = get(p, -1, 0)
        elif char == '>':
            element = get(p, 0, +1)
        elif char == '<':
            element = get(p, 0, -1)

        if i % 2 == 0:
            p_santa = element
        else:
            p_robot = element

        result.append(element)

    r = set(result)
    return r

if __name__ == '__main__':

    result = len(houses_of(input))
    print result
