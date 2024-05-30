from queue import PriorityQueue

def tsp_heuristic(graph, path):
    # Lista cu orasele nevizitate (toate orasele din graf care nu sunt in drumul curent)
    unvisited_cities = [city for city in range(len(graph)) if city not in path]
    if unvisited_cities:
        # Gasirea distantei minime de la ultimul oras vizitat la un oras nevizitat
        min_last_to_unvisited = min(graph[path[-1]][city] for city in unvisited_cities)
        # Calcularea sumei distantelor minime de la fiecare oras nevizitat la orice oras din drumul curent
        min_unvisited_to_start = sum(min(graph[city][start] for start in path) for city in unvisited_cities)
        # Returneaza suma celor doua valori ca valoare euristica
        return min_last_to_unvisited + min_unvisited_to_start
    else:
        # Daca toate orasele sunt vizitate, returneaza 0 ca valoare euristica
        return 0

def tsp_a_star(graph):
    n = len(graph)  # Numarul de orase in graf
    start_node = (0, [0])  # Nodul de pornire (cost total, drum)
    pq = PriorityQueue()  # Coada de prioritati pentru A*
    pq.put(start_node)  # Adauga nodul de start in coada de prioritati

    while not pq.empty():
        total_cost, path = pq.get()  # Extrage nodul cu costul total minim si drumul asociat
        if len(path) == n:
            # Daca toate orasele au fost vizitate, returneaza drumul completat cu orasul de start la final
            return path + [0]
        
        last_city = path[-1]  # Ultimul oras vizitat
        unvisited_cities = [city for city in range(n) if city not in path]  # Lista oraselor nevizitate
        if unvisited_cities:
            # Gaseste distanta minima de la ultimul oras vizitat la orice oras nevizitat
            min_last_to_unvisited = min(graph[last_city][city] for city in unvisited_cities)
            for city in unvisited_cities:
                # Creeaza un nou drum adaugand orasul nevizitat curent
                new_path = path + [city]
                # Calculeaza noul cost total adaugand distanta la orasul nevizitat curent
                new_cost = total_cost + graph[last_city][city]
                # Calculeaza valoarea euristica pentru noul drum
                heuristic = tsp_heuristic(graph, new_path)
                # Adauga noul nod in coada de prioritati
                pq.put((new_cost + heuristic, new_path))
        else:
            # Daca toate orasele au fost vizitate, returneaza drumul completat cu orasul de start la final
            return path + [0]
