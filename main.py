from libs.random_bit import random_insert_space

space_size, bit25, first_impro = random_insert_space()

count_row = 1
print("="*70+"space_size"+"="*70)
for row in space_size:
    print("{} - {}".format(count_row, row))
    count_row += 1

print("="*150)
print("First-improvement : {}".format(first_impro))
print("25 bit problem : ", bit25)
