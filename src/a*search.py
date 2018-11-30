from implementation import *

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    distX = abs(x1 - x2)
    distY = abs(y1 - y2)

    if distX > distY:
        return distY * 14 + 10 * (distX - distY)
    return distX * 14 + 10 * (distY - distX)


def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far


start, goal = (0, 9), (9, 0)
came_from, cost_so_far = a_star_search(diagram4, start, goal)
draw_grid(diagram4, width=4, start=start, goal=goal)
print()
draw_grid(diagram4, width=4, point_to=came_from, start=start, goal=goal)
print()
draw_grid(diagram4, width=4, number=cost_so_far, start=start, goal=goal)
print()