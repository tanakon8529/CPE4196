from random import randrange

def random_bit():
    space_size = []
    for count in range(10):
        space_in = []
        for count in range(5):
            space_in.append(randrange(2))

        space_size.append(space_in)


    bit_25 = []
    first_impro = []
    for count in range(25):
        x = randrange(10)
        y = randrange(5)
        if first_impro == []:
            first_impro = "[{}][{}]".format(x+1, y+1)
        bit_25.append(space_size[x][y])

    return space_size, bit_25, first_impro
