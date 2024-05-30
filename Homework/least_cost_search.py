from queue import PriorityQueue

def tsp_least_cost(graph):
    n = len(graph)
    pq = PriorityQueue()
    pq.put((0, [0]))  # (total_cost, path)

    while not pq.empty():
        total_cost, path = pq.get()
        # Daca am vizitat toate orasele, returnam calea
        if len(path) == n:
            return path + [0]
        
        last_city = path[-1]
        # Iteram prin toate orasele
        for city in range(n):
            # Verificam daca orasul nu a fost vizitat
            if city not in path:
                # Generam o noua cale adaugand orasul curent
                new_path = path + [city]
                # Calculam noul cost
                new_cost = total_cost + graph[last_city][city]
                # Adaugam noul nod in coada de prioritate
                pq.put((new_cost, new_path))