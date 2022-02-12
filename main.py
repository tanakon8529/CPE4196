from libs.random_bit import random_insert_space

# ---select algorithm---
# hill_climbing
# simulated_annealing
# tabu_search
option = "tabu_search"
result_pack = random_insert_space(option)

if option == "tabu_search":
    print("\ntabu_search [{}] : {}".format(len(result_pack[6]), result_pack[6]))

else:
    print("\nbit_init : ", result_pack[0])
    print("init decimal : ", result_pack[1])
    print("First improvement : ",  result_pack[2])
    print("First decimal : ", result_pack[3])
    print("Best improvement : ", result_pack[4])
    print("Worst improvement : ", result_pack[5])


