from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def build_graph(self, amount_of_nodes, edges):
        for i in range(1, amount_of_nodes+1):
            self.graph[i] = []

        for i in range(len(edges)):
            self.graph[edges[i][0]].append(edges[i][1])
            self.graph[edges[i][1]].append(edges[i][0])



    def bfs(self, amount_of_nodes, amount_of_edges, edges, starting_node):
        self.build_graph(amount_of_nodes, edges)

        visited = [False]*(len(self.graph)+1)
        visited[0] = True
        queue = []

        queue.append(starting_node)
        levels = defaultdict(list)
        visited[starting_node] = True
        output = [-1]*(len(self.graph)+1)
        weight = 6

        while queue:
            state = False  #Check if node has adjesent unvisited nodes
            s = queue.pop(0)
            if s == starting_node:
                levels[0].append(s)
            for i in self.graph[s]:
                for key, values in levels.items():
                    if s in values:
                        levels[key+1].append(i)
                        break

                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    for key, value in levels.items():
                        if i in value:
                            output[i] = 6 * key

        output.pop(0)
        output.pop(starting_node-1)
        self.clear_graph()
        return output
    
    def clear_graph(self):
        self.graph.clear()


g =  Graph()
print(g.bfs(4,2,[[1,2],[1,3]],2))