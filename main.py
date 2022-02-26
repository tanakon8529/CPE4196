from libs.metaheuristics import search_meta

# ---select algorithm---
# hill_climbing
# simulated_annealing
# tabu_search
# iterated_local_search
# general_variable_neighbourhood_search

algorrithm_search = search_meta()
option = "general_variable_neighbourhood_search"
result_pack = algorrithm_search.algorithms_search(option)

if option == "tabu_search":
    print("\ntabu_search [{}] : {}".format(len(result_pack[6]), result_pack[6]))

if option == "general_variable_neighbourhood_search":
    print("\nGVNS : bit best sulotion : [{}]".format(result_pack[7]))
    print("GVNS : decimal best sulotion : [{}]".format(result_pack[8]))
    
else:
    print("\nbit_init : ", result_pack[0])
    print("init decimal : ", result_pack[1])
    print("First improvement : ",  result_pack[2])
    print("First decimal : ", result_pack[3])
    print("Best improvement : ", result_pack[4])
    print("Worst improvement : ", result_pack[5])
