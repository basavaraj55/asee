import random
import sys
sys.setrecursionlimit(10000)  # Allow deep recursion for large mazes

class Maze:
    def __init__(self, width, height):
        if width < 3 or height < 3:
            raise ValueError("Maze dimensions must be at least 3x3.")
        self.width = width
        self.height = height
        self.grid = [["#" for _ in range(width)] for _ in range(height)]
        self.visited = [[False for _ in range(width)] for _ in range(height)]

    def generate(self, x=1, y=1):
        """Recursive backtracking maze generation."""
        self.visited[y][x] = True
        self.grid[y][x] = " "
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < self.width - 1 and 1 <= ny < self.height - 1:
                if not self.visited[ny][nx]:
                    self.grid[y + dy // 2][x + dx // 2] = " "
                    self.generate(nx, ny)

    def display(self):
        for row in self.grid:
            print("".join(row))

    def solve(self, start=(1, 1), end=None):
        """DFS maze solver."""
        if end is None:
            end = (self.width - 2, self.height - 2)
        path = []
        visited = set()

        def dfs(x, y):
            if (x, y) == end:
                path.append((x, y))
                return True
            if (x, y) in visited or self.grid[y][x] == "#":
                return False
            visited.add((x, y))
            path.append((x, y))
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if dfs(x + dx, y + dy):
                    return True
            path.pop()
            return False

        dfs(*start)
        for x, y in path:
            if (x, y) != start and (x, y) != end:
                self.grid[y][x] = "."
        return path


# ------------------ MAIN EXECUTION ------------------
try:
    maze = Maze(width=21, height=15)  # Odd dimensions work best
    maze.generate()
    print("Generated Maze:")
    maze.display()

    print("\nSolving Maze...")
    path = maze.solve()
    maze.display()
    print(f"\nPath length: {len(path)} steps")

except Exception as e:
    print(f"Error: {e}")
