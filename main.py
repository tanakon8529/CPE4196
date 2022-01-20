from libs.random_bit import random_insert_space

result_pack, space_size = random_insert_space()

print("bit_init : ", result_pack[0])
print("init decimal : ", result_pack[1])

print("first improvement : ",  result_pack[2])
print("first index : ", result_pack[3])
print("first decimal : ", result_pack[4])

print("="*50+"space_size"+"="*50)
print(space_size)

