from random import randrange

def random_25_bit(size):
    bit_25 = []
    for binary in range(size):
        bit_25.append(randrange(2))

    return bit_25

def random_insert_space():
    space_size = []
    for count in range(25):
        space_in = []
        for count in range(2):
            space_in.append(random_25_bit(25))

        space_size.append(space_in)

    choice_25_bit = []
    first_impro = []
    for count in range(25):
        x = randrange(25)
        y = randrange(2)
        if first_impro == []:
            first_impro = "[{}][{}]".format(x+1, y+1)
        choice_25_bit.append(space_size[x][y])
        if choice_25_bit:
            break

    return space_size, choice_25_bit[0], first_impro
