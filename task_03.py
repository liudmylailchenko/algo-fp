import heapq


def dijkstra(graph, start, goal):
    distances = {vertex: float("inf") for vertex in graph}
    print("distances", distances)
    distances[start] = 0

    priority_queue = [(0, start)]
    print("priority_queue", priority_queue)
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex == goal:
            return current_distance

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return float("inf")


graph = {
    "A": [("B", 1), ("C", 4), ("E", 7)],
    "B": [("A", 1), ("C", 2), ("D", 5)],
    "C": [("A", 4), ("B", 2), ("D", 1), ("E", 3)],
    "D": [("B", 5), ("C", 1), ("E", 2), ("F", 6)],
    "E": [("A", 7), ("C", 3), ("D", 2), ("F", 4)],
    "F": [("D", 6), ("E", 4)],
}

start_vertex = "A"
goal_vertex = "D"
shortest_path_distance = dijkstra(graph, start_vertex, goal_vertex)
print(
    f"Shortest path distance from {start_vertex} to {goal_vertex}: {shortest_path_distance}"
)
