

def analize(line):
    instr = [i.strip() for i in line.split(' ')]

    r = dict()

    if len(instr) == 4:
        r['instr'] = 'toggle'
    else:
        if instr[1] == 'on':
            r['instr'] = 'on'
        elif instr[1] == 'off':
            r['instr'] = 'off'

    r['to'] = [int(i) for i in instr[len(instr) - 1].split(',')]
    r['from'] = [int(i) for i in instr[len(instr) - 3].split(',')]

    return r


def apply_instr_1(instr, lights):

    for i in range(instr['from'][0], instr['to'][0] + 1):
        for j in range(instr['from'][1], instr['to'][1] + 1):
            if instr['instr'] == 'toggle':
                lights[i][j] = int(not lights[i][j])
            elif instr['instr'] == 'off':
                lights[i][j] = 0

            elif instr['instr'] == 'on':
                lights[i][j] = 1


def apply_instr_2(instr, lights):

    for i in range(instr['from'][0], instr['to'][0] + 1):
        for j in range(instr['from'][1], instr['to'][1] + 1):
            if instr['instr'] == 'toggle':
                lights[i][j] += 2
            elif instr['instr'] == 'off':
                lights[i][j] = max(0, lights[i][j] - 1)
            elif instr['instr'] == 'on':
                lights[i][j] += 1

if __name__ == '__main__':

    lights = [[0 for x in range(1000)] for x in range(1000)]

    with open('./input.txt', 'r') as fd:
        for line in fd.readlines():
            instr = analize(line)
            apply_instr_2(instr, lights)

    # result = 0
    # for i in range(len(lights)):
    #    result += lights[i].count(1)
    #
    # print result

    print sum(map(sum, lights))
