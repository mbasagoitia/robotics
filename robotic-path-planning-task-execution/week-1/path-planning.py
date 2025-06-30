import numpy as np
import matplotlib.pyplot as plt
from collections import deque, defaultdict
from heapq import heapify, heappush, heappop

def get_neighbors(grid, pos):
    i, j = pos

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    neighbors = []

    # Wormhole
    # if pos == (0, 5):
    #     return [(0, (15, 15))]

    for di, dj in directions:
        new_i, new_j = i + di, j + dj
        if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]):
            if grid[new_i][new_j] < 0.3:
                cost = np.sqrt(di**2 + dj**2)
                neighbors.append((cost, (new_i, new_j)))

    return neighbors

def bfs(grid, start, goal):
    queue = deque([start])
    visited = set([start])
    parents = {}

    while queue:
        current = queue.popleft()
        if current == goal:
            break
        for cost, neighbor in get_neighbors(grid, current):
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current
                queue.append(neighbor)
                plt.plot(neighbor[1], neighbor[0], 'g*')
                plt.pause(0.00001)

    # Reconstruct path
    path = []
    node = goal
    while node in parents:
        path.append(node)
        node = parents[node]
    path.append(start)
    path.reverse()
    return path

def dijkstra(grid, start, goal):
    heap = []
    heapify(heap)
    heappush(heap, (0, start))

    visited = set()
    parents = {}

    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0

    while heap:
        dist, current = heappop(heap)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            break

        for cost, neighbor in get_neighbors(grid, current):
            if neighbor not in visited:
                new_dist = dist + cost
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    parents[neighbor] = current
                    heappush(heap, (new_dist, neighbor))
                    plt.plot(neighbor[1], neighbor[0], 'b.')
                    plt.pause(0.00001)

    # Reconstruct path
    path = []
    node = goal
    while node in parents:
        path.append(node)
        node = parents[node]
    path.append(start)
    path.reverse()
    return path

def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def astar(grid, start, goal):
    heap = []
    heapify(heap)
    heappush(heap, (euclidean_distance(start, goal), 0, start))

    visited = set()
    parents = {}

    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
   
    while heap:
        estimated, current_distance, current = heappop(heap)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            break

        for cost, neighbor in get_neighbors(grid, current):
            if neighbor not in visited:
                new_cost = current_distance + cost
                if new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    estimated = new_cost + euclidean_distance(neighbor, goal)
                    parents[neighbor] = current
                    heappush(heap, (estimated, new_cost, neighbor))
                    plt.plot(neighbor[1], neighbor[0], 'c.')
                    plt.pause(0.00001)

    # Reconstruct path
    path = []
    node = goal
    while node in parents:
        path.append(node)
        node = parents[node]
    path.append(start)
    path.reverse()
    return path

def map_to_world(map_pos):
    scale = 0.05
    origin = (0, 0)

    i, j = map_pos

    x = origin[0] + j * scale
    y = origin[1] + i * scale

    return (x, y)

rows, cols = 20, 30
np.random.seed(42)
grid = (np.random.rand(rows, cols) < 0.2).astype(float)
start = (0, 0)
goal = (19, 29)
grid[goal] = 0

plt.ion()
plt.imshow(grid, cmap='Greys')
plt.plot(goal[1], goal[0], 'y*')

# path = bfs(grid, start, goal)
# path = dijkstra(grid, start, goal)
path = astar(grid, start, goal)

for p in path:
    plt.plot(p[1], p[0], 'r.')

plt.ioff()
plt.show()
