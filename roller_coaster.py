

class RollerCoaster:
    def __init__(self):
        self.max_length = 0
        self.coaster_path = []
        self.start_pos = []



    # @return the length of the longest drop of the coaster
     # Method to compute the longest downhill slope of the roller coaster
    def compute(self, terrain):
        # Get the number of rows and columns in the terrain grid
        rows = len(terrain)
        cols = len(terrain[0])

        # Initialize a 2D array to store lengths of longest downhill slopes starting from each cell
        dp = [[0] * cols for _ in range(rows)]

        # Define possible directions to move (up, down, left, right)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # Function to check if a move from (x, y) to (nx, ny) is valid
        def is_valid_move(x, y, nx, ny):
            return 0 <= nx < rows and 0 <= ny < cols and terrain[x][y] > terrain[nx][ny]

        # Depth-first search (DFS) function to find the longest downhill slope starting from (x, y)
        def dfs(x, y):
            # If the length from (x, y) has already been computed, return it
            if dp[x][y] > 0:
                return dp[x][y]

            max_length_here = 0

            # Explore all possible directions from the current cell
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # If the move is valid, find the length of the downhill slope starting from the new cell
                if is_valid_move(x, y, nx, ny):
                    max_length_here = max(max_length_here, dfs(nx, ny))

            # Store the length of the longest downhill slope starting from (x, y)
            dp[x][y] = max_length_here + 1
            return dp[x][y]

        # Iterate over all cells to find the longest downhill slope starting from each cell
        for i in range(rows):
            for j in range(cols):
                length_here = dfs(i, j)
                # Update the maximum length and starting position of the coaster's drop if needed
                if length_here > self.max_length:
                    self.max_length = length_here
                    self.start_pos = [i, j]

        # Find the path of the coaster based on the computed longest downhill slope
        self.find_coaster_path(terrain, dp)

        # Return the length of the longest downhill slope
        return self.max_length

    # Method to find the path of the coaster based on the computed longest downhill slope
    def find_coaster_path(self, terrain, dp):
        x, y = self.start_pos
        self.coaster_path.append(terrain[x][y])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # Traverse the grid based on the computed longest downhill slope
        while True:
            max_length_here = dp[x][y]
            next_x, next_y = x, y

            # Find the next cell in the coaster path
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(terrain) and 0 <= ny < len(terrain[0]) and dp[nx][ny] == max_length_here - 1:
                    next_x, next_y = nx, ny
                    break

            # Break if the next cell is the same as the current cell
            if next_x == x and next_y == y:
                break

            # Add the elevation of the next cell to the coaster path
            self.coaster_path.append(terrain[next_x][next_y])
            x, y = next_x, next_y

    # Getter method to return the coaster path
    def getCoasterPath(self):
        return self.coaster_path

    # Getter method to return the starting position of the coaster's drop
    def getCoasterStart(self):
        return self.start_pos