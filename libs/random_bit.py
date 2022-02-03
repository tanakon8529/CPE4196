from random import randrange

def listToString(s):
    str1 = ""

    for ele in s:
        str1 += str(ele)
        
    return str1

def bit_flip(bit):
    bit_new = []
    for bit_ele in bit:
        
        if bit_ele == '1':
            bit_ele = '0'
        else:
            bit_ele = '1'

        bit_new.append(bit_ele)
    
    bit_new_string = listToString(bit_new)
    return bit_new_string

def random_25_bit(size):
    bit_25 = []
    bit_25_string = []
    for binary in range(size):
        bit_25.append(randrange(2))
    
    bit_25_string.append(listToString(bit_25))

    return bit_25_string[0]

def random_insert_space():
    result_pack = []
    bit_to_init = None
    bit_init = None
    first_impro = None
    worst_impro_index = 0
  
    for round in range(50):
        space_size = []
        position_i = 0
        position_j = 0
        for round_in in range(50):
            details_item = [random_25_bit(25), position_i, position_j]
            space_size.append(details_item)
            if position_j == 4:
                position_i += 1
                position_j = -1

            position_j += 1

        if bit_init == None:
            bit_init = space_size[0][0]
            bit_to_init = int(space_size[0][0], 2)
            result_pack.append(bit_init)
            result_pack.append(bit_to_init)

        count = 0
        for item in space_size:

            item_bit_flip = bit_flip(item[0])

            if bit_to_init < int(item_bit_flip, 2):
                bit_init, bit_to_init = item_bit_flip, int(item_bit_flip, 2)
                first_impro = item_bit_flip

                if worst_impro_index < space_size.index(item):
                    best_impro_index = worst_impro_index
                    worst_impro_index = space_size.index(item)
                break


            count += 1

    result_pack.append(first_impro)
    result_pack.append(bit_to_init)
    result_pack.append(best_impro_index)
    result_pack.append(worst_impro_index)
    
    return result_pack, space_size
