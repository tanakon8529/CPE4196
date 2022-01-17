from libs.random_bit import random_bit

space_size, bit25, first_impro = random_bit()

print("===space_size===")
for row in space_size:
    print(row)
print("===============")
print("First-improvement : {}".format(first_impro))
print("25 bit problem : ", bit25)
