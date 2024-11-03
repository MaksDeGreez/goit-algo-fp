import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[from_node].append((weight, to_node))
        self.edges[to_node].append((weight, from_node))

def dijkstra(graph, start):
    distances = { node: float('inf') for node in graph.edges }
    distances[start] = 0
    priority_queue = [(0, start)] # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for weight, neighbor in graph.edges[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def main():
    graph = Graph()
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 1)

    start_node = 'A'
    distances = dijkstra(graph, start_node)

    print(f"Shortest paths from node {start_node}:")
    for node, distance in distances.items():
        print(f"Distance to {node}: {distance}")

if __name__ == "__main__":
    main()
