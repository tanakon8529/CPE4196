from random import randrange
from unittest import result


def listToString(s):
    str1 = ""

    for ele in s:
        str1 += str(ele)
        
    return str1

def random_25_bit(size):
    bit_25 = []
    bit_25_string = []
    for binary in range(size):
        bit_25.append(randrange(2))
    
    bit_25_string.append(listToString(bit_25))

    return bit_25_string

def random_insert_space():
    space_size = []
    result_pack = []
    bit_to_int = None
    bit_init = None
    
    for count in range(50):
        space_size.append(random_25_bit(25))
        bit_init = space_size[0][0]
        bit_to_int = int(space_size[0][0], 2)
    
    result_pack.append(bit_init)
    result_pack.append(bit_to_int)


    count += 0
    for item in space_size:
        first_impro = None

        if bit_to_int < int(item[0], 2):
            first_impro, first_impro_index, bit_to_int_first = item[0], space_size.index(item), int(item[0], 2)
            break

        count += 1

    result_pack.append(first_impro)
    result_pack.append(first_impro_index)
    result_pack.append(bit_to_int_first)
        
    return result_pack, space_size
