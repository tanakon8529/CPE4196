from libs.random_bit import random_insert_space
from tabulate import tabulate

result_pack, space_size = random_insert_space()

print("\nbit_init : ", result_pack[0])
print("init decimal : ", result_pack[1])

print("First improvement : ",  result_pack[2])
print("First decimal : ", result_pack[3])
print("Best improvement : ", result_pack[4])
print("Worst improvement : ", result_pack[5])

# position in table
print(tabulate(space_size, headers=['25bit', 'position i', 'position j']))

# print(space_size)

