# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        # Set to store visited positions
        visited = set()
        # Directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def backtrack(x: int, y: int, cur_dir: int):
            # Mark current cell as visited and clean it
            visited.add((x, y))
            robot.clean()

            # Explore all 4 directions
            for i in range(4):
                new_dir = (cur_dir + i) % 4
                dx, dy = directions[new_dir]
                nx, ny = x + dx, y + dy

                if (nx, ny) not in visited:
                    if robot.move():  # Move succeeds
                        backtrack(nx, ny, new_dir)
                        # Backtrack: go back to previous cell and restore direction
                        robot.turnLeft()
                        robot.turnLeft()
                        robot.move()
                        robot.turnLeft()
                        robot.turnLeft()
                # Turn the robot to the next direction
                robot.turnRight()

        # Start DFS from initial position (0, 0) facing up (direction 0)
        backtrack(0, 0, 0)
        