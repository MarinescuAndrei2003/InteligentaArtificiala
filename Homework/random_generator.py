import random

def generate_tsp_graph(num_cities, min_distance=1, max_distance=100):
    graph = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = random.randint(min_distance, max_distance)
            graph[i][j] = distance
            graph[j][i] = distance  
    return graph