import heapq
import itertools
from timeit import default_timer as timer
from datetime import timedelta
from dfs import tsp_dfs_wrapper
from least_cost_search import tsp_least_cost
from a_star import tsp_a_star
from random_generator import generate_tsp_graph

#City:
#0 - Bucuresti
#1 - Cluj
#2 - Timisoara
#3 - Iasi
#4 - Constanta

# Bucuresti[0] -> Constanta[4] -> Iasi[3] -> Cluj[1] -> Timisoara[2] -> Bucuresti[0]
# Bucuresti[0] -> Timisoara[2] -> Cluj[1] -> Iasi[3] -> Constanta[4] -> Bucuresti[0]

graph = [[0, 450, 530, 410, 225],
         [450, 0, 320, 380, 600],
         [530, 320, 0, 500, 550],
         [410, 380, 500, 0, 370],
         [225, 600, 550, 370, 0]]

start = timer()
print(tsp_dfs_wrapper(graph))
end = timer()
print("DFS: ", timedelta(seconds=end-start))

start = timer()
print(tsp_least_cost(graph))
end = timer()
print("Least_cost_search: ", timedelta(seconds=end-start))

start = timer()
print(tsp_a_star(graph))
end = timer()
print("A* search:  ", timedelta(seconds=end-start))

print("-------------------------------------------------------------------------")

graph1 = generate_tsp_graph(10)

print("graph1:\n", graph1)


start = timer()
print(tsp_dfs_wrapper(graph1))
end = timer()
print("DFS: ", timedelta(seconds=end-start))


start = timer()
print(tsp_least_cost(graph1))
end = timer()
print("Least_cost_search: ", timedelta(seconds=end-start))


start = timer()
print(tsp_a_star(graph1))
end = timer()
print("A* search:  ", timedelta(seconds=end-start))