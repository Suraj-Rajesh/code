from Queue import Queue

graph_1 = {
     'a': ['c'],
     'b': ['c', 'e'],
     'c': ['a', 'b', 'd', 'e'],
     'd': ['c'],
     'e': ['b', 'c', 'f'],
     'f': []
     }


graph = {
        1: [2, 4, 5],
        2: [1, 7, 3, 6],
        4: [1],
        5: [1],
        6: [2],
        7: [2],
        3: [2]
        }

def dfs(graph, vertex, res_list=[]):
    if vertex not in res_list:
        res_list.append(vertex)

        # visit neighbours
        for neighbour in graph[vertex]:
            # explore
            dfs(graph, neighbour, res_list)


def bfs(graph, vertex):
    res_list = []
    queue = Queue()

    # initialize
    queue.put(vertex)
    res_list.append(vertex)

    # process
    while not queue.empty():
        cur_vertex = queue.get()

        for neighbour in graph[cur_vertex]:
            if neighbour not in res_list:
                queue.put(neighbour)
                res_list.append(neighbour)

    return res_list

print bfs(graph, 1)

dfs_res = []
dfs(graph, 1, dfs_res)
print dfs_res
