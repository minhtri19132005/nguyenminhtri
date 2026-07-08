import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_node in visited:
            continue
        visited.add(current_node)
        
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances


def bellman_ford(graph, start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                print("Đồ thị chứa chu trình âm!")
                return None
                
    return distances

graph = {
    'A': {'B': 3, 'C': 5},
    'B': {'C': -3},
    'C': {}
}

dijkstra_result = dijkstra(graph, 'A')
print(f"Kết quả từ Dijkstra:    {dijkstra_result}")
print(f"  > Đường đi ngắn nhất tới C theo Dijkstra là: {dijkstra_result['C']} (Sai vì đi trực tiếp A -> C)")

print("-" * 50)

bellman_result = bellman_ford(graph, 'A')
print(f"Kết quả từ Bellman-Ford: {bellman_result}")
print(f"  > Đường đi ngắn nhất tới C chính xác phải là: {bellman_result['C']} (Đúng vì đi qua đường A -> B -> C = 3 + (-3) = 0)")