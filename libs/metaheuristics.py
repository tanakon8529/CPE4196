from random import randrange, choice

class search_meta(object):
    def __init__(self):
        self.criteria_iterations = 50
        self.size_bit = 25
        self.space_size = 50
        self.tabu_tenure = 20
        self.perturbation = 3
 
    def listToString(self, s):
        str1 = ""
        for ele in s:
            str1 += str(ele)
        return str1

    def bit_flip(self, bit):
        bit_new = []
        for bit_ele in bit:
            if bit_ele == '1':
                bit_ele = '0'
            else:
                bit_ele = '1'
            bit_new.append(bit_ele)

        bit_new_string = self.listToString(bit_new)
        return bit_new_string

    def random_bit(self, size):
        bit_25 = []
        bit_25_string = []
        for binary in range(size):
            bit_25.append(randrange(2))

        bit_25_string.append(self.listToString(bit_25))
        return bit_25_string[0]

    def random_position(self, bit):
        position = []
        max_bit = len(bit)
        for round in range(2):
            position.append(randrange(max_bit))

        return position

    def Exchange_position(self, bit, i, j):
        lst = list(bit)
        lst[i], lst[j] = lst[j], lst[i]
        return ''.join(lst)

    def insert_shift(self, bit, i, j):
        lst = list(bit)
        lst.insert(j, lst[i])
        lst.remove(lst[i])
        return ''.join(lst)

    def convert_list_bit_to_decimal(self, pack_bit):
        pack_bit_int = []
        for bit in pack_bit:
            bit_int = int(bit, 2)
            pack_bit_int.append(bit_int)

        return pack_bit_int

    def convert_list_decimal_to_bit(self, pack_int):
        pack_bit = []
        for item_int in pack_int:
            item_bit = f'{item_int:25b}'
            pack_bit.append(item_bit)

        return pack_bit

    def random_space_size(self, option):
        space_size = []
        for round_in in range(self.space_size):
            bit_item = self.random_bit(self.size_bit)
            position = self.random_position(bit_item)
            if option == "simulated_annealing" or option == "tabu_search" or option == "iterated_local_search":
                item_new = self.insert_shift(bit_item, position[0], position[1])
            if option == "hill_climbing":
                item_new = self.Exchange_position(bit_item, position[0], position[1])
                # item_new = self.bit_flip(bit_item)
            if option == "tabu_search":
                item_new = self.insert_shift(bit_item, position[0], position[1])
            if option == "iterated_local_search":
                item_new = self.insert_shift(bit_item, position[0], position[1])
            space_size.append(item_new)

        return space_size

    def hill_climbing(self, space_size, bit_init_int, first_impro, first_impro_int, round_impro):

        for item in space_size:
            item_int = int(item, 2)
            if item_int > bit_init_int:
                if item_int > first_impro_int:
                    first_impro = item
                    first_impro_int = item_int
                    round_impro = space_size.index(item)

        return first_impro, first_impro_int, round_impro

    def simulated_annealing(self, bit_init_int, space_size):
        best_impro = None
        worst_impro = None

        initial_temp = 1000
        final_temp = .1
        alpha = 0.01
        solution_int = 0
        current_temp = initial_temp
        current_state = bit_init_int
        solution = current_state

        while current_temp > final_temp:
            neighbor  = choice(space_size)
            neighbor_int = int(neighbor , 2)
            if current_temp == initial_temp:
                if neighbor_int > current_state:
                    solution = neighbor
                    solution_int = int(solution, 2)
            else:
                if neighbor_int > solution_int:
                    solution = neighbor
                    solution_int = int(solution, 2)

            current_temp -= alpha

        first_impro = solution
        first_impro_int = solution_int
        return first_impro, first_impro_int, best_impro, worst_impro

    def tabu_search_find_candidate(self, candidate_list, space_size):
    
        space_size_int = self.convert_list_bit_to_decimal(space_size)
        candidate_int = max(space_size_int)
        candidate = f'{candidate_int:25b}'
        candidate_list.append(candidate)

        return candidate_list

    def tabu_search_candi_max(self, candidate_list):
    
        tabu_list_int = []
        candidate_list_int = self.convert_list_bit_to_decimal(candidate_list)
        for count in range(self.tabu_tenure):
            candi_max = max(candidate_list_int)
            tabu_list_int.append(candi_max)
            if candi_max in tabu_list_int:
                candidate_list_int.remove(candi_max)
        tabu_list = self.convert_list_decimal_to_bit(tabu_list_int)

        return tabu_list

    def iterated_local_search(self, space_size, bit_init, first_impro, first_impro_int, round_impro):
    
        for perturb in range(self.perturbation):
            position = self.random_position(bit_init)
            new_item = self.Exchange_position(bit_init, position[0], position[1])
        bit_init_int = int(new_item, 2)
        first_impro, first_impro_int, round_impro = self.hill_climbing(space_size, bit_init_int, first_impro, first_impro_int, round_impro)

        return first_impro, first_impro_int, round_impro

    def algorithms_search(self, option):
        result_pack = []
        candidate_list = []
        tabu_list = []
        best_impro = None
        round_impro = 0
        worst_impro = 0
        

        for round in range(self.criteria_iterations):
            space_size = self.random_space_size(option)
            bit_init = space_size[0]
            bit_init_int = int(bit_init, 2)
            first_impro = bit_init
            first_impro_int = bit_init_int

            if option == "hill_climbing":
                first_impro, first_impro_int, round_impro = self.hill_climbing(space_size, bit_init_int, first_impro, first_impro_int, round_impro)
                if best_impro == None:
                    best_impro = round_impro
                if round_impro < best_impro:
                    best_impro = round_impro
                if round_impro > worst_impro:
                    worst_impro = round_impro
                
            if option == "simulated_annealing":
                first_impro, first_impro_int, best_impro, worst_impro = self.simulated_annealing(bit_init_int, space_size)

            if option == "tabu_search":
                candidate_list = self.tabu_search_find_candidate(candidate_list, space_size)

            if option == "iterated_local_search":
                first_impro, first_impro_int, round_impro = self.iterated_local_search(space_size, bit_init, first_impro, first_impro_int, round_impro)
                if best_impro == None:
                    best_impro = round_impro
                if round_impro < best_impro:
                    best_impro = round_impro
                if round_impro > worst_impro:
                    worst_impro = round_impro

        if option == "tabu_search":
            tabu_list = self.tabu_search_candi_max(candidate_list)

        result_pack.append(bit_init)
        result_pack.append(bit_init_int)
        result_pack.append(first_impro)
        result_pack.append(first_impro_int)
        result_pack.append(best_impro)
        result_pack.append(worst_impro)
        result_pack.append(tabu_list)

        return result_pack
