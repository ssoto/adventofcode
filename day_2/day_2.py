

from challenge_input import input

def get_boxes(a_input):
    result = []
    for line in a_input.split('\n'):
        sizes = map(lambda x: int(x), line.split('x'))
        result.append(sizes)
    return result


if __name__ == '__main__':
    boxes = get_boxes(input)
    result = 0
    for box in boxes:
        box.sort()
        result += box[0] * 2 + box[1] * 2
        result += box[0] * box[1] * box[2]
    print result
