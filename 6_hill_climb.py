import random

graph = [[0, 400, 500, 300], [600, 0, 300, 500], [500, 300, 0, 400], [900, 500, 400, 0]]


def rand_cities():
    temp_lst = list(range(len(graph)))
    result = []
    for i in range(len(graph)):
        randomCity = temp_lst[random.randint(0, len(temp_lst) - 1)]
        result.append(randomCity)
        temp_lst.remove(randomCity)
    return result


def tot_len(lst):
    tot_len = 0
    for i in range(len(graph)):
        try:
            tot_len += graph[lst[i]][lst[i + 1]]
        except IndexError:
            tot_len += graph[lst[i]][lst[0]]
    return tot_len


def generate_neighbours(lst):
    neighbours_lst = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            neighbour = lst.copy()
            neighbour[i] = lst[j]
            neighbour[j] = lst[i]
            neighbours_lst.append(neighbour)
    return neighbours_lst


def best_neighbour_fn(neighbours_lst):
    best_neighbour = neighbours_lst[0]
    best_tot_len = tot_len(neighbours_lst[0])
    for neighbour in neighbours_lst:
        current_tot_len = tot_len(neighbour)
        if current_tot_len < best_tot_len:
            best_neighbour = neighbour
            best_tot_len = current_tot_len
    return best_neighbour, best_tot_len


def hill_climbing():
    current_result = rand_cities()
    current_tot_len = tot_len(current_result)
    neighbours = generate_neighbours(current_result)
    best_neighbour, best_tot_len = best_neighbour_fn(neighbours)
    while current_tot_len > best_tot_len:
        current_result = best_neighbour
        current_tot_len = best_tot_len
        neighbours = generate_neighbours(current_result)
        best_neighbour, best_tot_len = best_neighbour_fn(neighbours)
    return current_result, current_tot_len


ans = hill_climbing()
print("Resulted route:", ans[0], "\nPath Cost:", ans[1])
