from libs.random_bit import random_insert_space

result_pack, space_size = random_insert_space()

print("\nbit_init : ", result_pack[0])
print("init decimal : ", result_pack[1])

print("First improvement : ",  result_pack[2])
print("First decimal : ", result_pack[3])
print("Best improvement : ", result_pack[4])
print("Worst improvement : ", result_pack[5])

print("="*50+"space_size"+"="*50)
print(space_size)

