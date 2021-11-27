class Robot:
    def move(self):
        pass
    def turnLeft(self):
        pass
    def turnRight(self):
        pass
    def clean(self):
        pass

class Solution:
    # Clockwise || Right Wall Following
    directions = [
        (1,  0),  # Up
        (0,  1),  # Right
        (-1, 0),  # Down
        (0, -1)   # Left
    ]

    def cleanRoom(self, robot):
        self.robot = robot
        self.visitedCells = set()
        self.curPos = (0,0)
        self.nextMove(0)
    
    def goBack(self):
        self.robot.turnRight()
        self.robot.turnRight()
        self.robot.move()
        self.robot.turnRight()
        self.robot.turnRight()

    def nextMove(self, d):
        self.robot.clean()
        self.visitedCells.add(self.curPos)
        #print(f"** Cleaned cell: {self.curPos}")

        # Move in all 4 directions
        for i in range(4):
            # Derive next cell's coordinates
            new_d = (d + i) % 4
            nextDir = self.directions[new_d]
            nextCell = (self.curPos[0] + nextDir[0], self.curPos[1] + nextDir[1])
            #print(f"[DEBUG] nextDir = {nextDir}")
            #print(f"[DEBUG] nextCell = {nextCell}")

            # Move if the nextCell hasn't already been visited && it's possible to move into the cell
            if not (nextCell in self.visitedCells):
                if self.robot.move():
                    oldPos = self.curPos
                    self.curPos = nextCell
                    self.nextMove(new_d)
                    # Return to previous cell
                    self.goBack()
                    self.curPos = oldPos
            # Always turnRight() before next iteration
            self.robot.turnRight()
