graph = {'A':set(['B','C','F']),
         'B':set(['D','A']),
         'C':set(['A','E']),
         'D':set(['G','B']),
         'E':set(['G','C']),
         'F':set(['A','G']),
         'G':set(['D','E','F'])
}
visited=set()

def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

print("dfs traversing without repitation")
dfs(visited,graph,'A')