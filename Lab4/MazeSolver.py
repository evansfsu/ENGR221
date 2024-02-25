"""
MazeSolver by Evan Schneider modified from code by Prof. Kabota
"""
from .SearchStructures import Stack, Queue
from .Maze import Maze

class MazeSolver:
    def __init__(self, maze, structure):
        self.maze = maze
        self.structure = structure()
        self.solution = None

    def solve(self):
        start = self.maze.find_start()
        goal = self.maze.find_goal()
        if start is None or goal is None:
            return None  # Handle case where start or goal is missing

        frontier = self.structure()
        frontier.push(start)
        came_from = {}
        came_from[start] = None

        while not frontier.is_empty():
            current = frontier.pop()
            if current == goal:
                break
            for neighbor in self.maze.get_neighbors(current):
                if neighbor not in came_from:
                    frontier.push(neighbor)
                    came_from[neighbor] = current

        if goal not in came_from:
            return None  # Handle case where no solution is found

        # Trace back from goal to start to find the path
        path = []
        current = goal
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()
        return path

    def printSolution(self):
        path = self.solve()
        if path is None:
            print("No solution found")
            return

        for row in self.maze.contents:
            row_str = ""
            for tile in row:
                if tile in path:
                    row_str += "*"
                else:
                    row_str += str(tile)
            print(row_str)