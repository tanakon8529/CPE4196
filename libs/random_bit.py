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

def random_position(bit):
    position = []
    max_bit = len(bit)
    for round in range(2):
        position.append(randrange(max_bit))

    return position

def swap_position(bit, i, j):
        lst = list(bit)
        lst[i], lst[j] = lst[j], lst[i]
        return ''.join(lst)
    

def random_insert_space():
    result_pack = []
    bit_to_init = None
    bit_init = None
    first_impro = None
    worst_impro_index = 0
  
    for round in range(50):
        space_size = []
        for round_in in range(50):
            details_item = random_25_bit(25)
            space_size.append(details_item)

        if bit_init == None:
            bit_init = space_size[0]
            bit_to_init = int(space_size[0], 2)
            result_pack.append(bit_init)
            result_pack.append(bit_to_init)

        count = 0
        for item in space_size:

            item_bit_flip = bit_flip(item)
            position = random_position(bit_init)
            bit_init_swap = swap_position(bit_init, position[0], position[1])
            bit_init_swap_int = int(bit_init_swap, 2)
 
            if bit_init_swap_int < int(item_bit_flip, 2):
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
