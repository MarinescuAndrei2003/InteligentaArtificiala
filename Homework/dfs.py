def tsp_dfs(graph, current_city, visited, count, path_length, min_path_length, path, min_path):
    # Daca toate orasele au fost vizitate
    if count == len(graph):
        # Adauga distanta de la orasul curent inapoi la orasul de start
        path_length += graph[current_city][0]
        # Actualizeaza lungimea minima a drumului si drumul minim daca drumul actual este mai scurt
        if path_length < min_path_length[0]:
            min_path_length[0] = path_length
            min_path[0] = path[:]
        return

    # Parcurge toate orasele din graf
    for city in range(len(graph)):
        # Daca orasul nu a fost vizitat si exista un drum de la orasul curent la orasul considerat
        if not visited[city] and graph[current_city][city] != 0:
            visited[city] = True  # Marcheaza orasul ca vizitat
            path.append(city)  # Adauga orasul in drumul curent
            # Apeleaza recursiv functia pentru orasul urmator
            tsp_dfs(graph, city, visited, count + 1, path_length + graph[current_city][city], min_path_length, path, min_path)
            path.pop()  # Elimina orasul din drumul curent (backtrack)
            visited[city] = False  # Marcheaza orasul ca nevizitat

def tsp_dfs_wrapper(graph):
    visited = [False] * len(graph)  # Lista pentru a tine evidenta oraselor vizitate
    visited[0] = True  # Marcheaza orasul de start ca vizitat
    min_path_length = [float('inf')]  # Initializeaza lungimea minima a drumului cu infinit
    min_path = [[]]  # Lista pentru a tine drumul minim
    # Apeleaza functia dfs pentru a gasi drumul minim
    tsp_dfs(graph, 0, visited, 1, 0, min_path_length, [0], min_path)
    # Asigura ca drumul include orasul de start la inceput si la final
    min_path[0].append(0)
    return min_path[0]  # Returneaza drumul minim
