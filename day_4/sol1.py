import md5

secret = 'yzbqklnj'


def mine(secret, starts):
    sol = ''
    for i in range(100000000):
        sol = md5.new('{}{}'.format(secret, i))
        if sol.hexdigest().startswith(starts):
            print '{}'.format(i)
            break


if __name__ == '__main__':
    #  mine(secret, '00000')
    mine(secret, '000000')
