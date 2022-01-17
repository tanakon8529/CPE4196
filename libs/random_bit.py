from random import randrange

def random_bit():
    space_size = []
    for count in range(10):
        space_in = []
        for count in range(5):
            space_in.append(randrange(2))

        space_size.append(space_in)


    bit_25 = []
    for count in range(25):
        bit_25.append(space_size[randrange(10)][randrange(5)])

    return bit_25
