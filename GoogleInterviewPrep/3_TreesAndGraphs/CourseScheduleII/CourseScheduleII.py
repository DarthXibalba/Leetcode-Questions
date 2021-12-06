"""
There are a total of numCourses courses you have to take, labeled from 0 to (numCourses-1).
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
 - For example, the pair [0, 1] indicates that to take course 0 you have to first take course 1

Return the ordering of courses you should take to finish all courses.
 - If there are many valid answers, return any of them.
 - If it is impossible to finish all courses, return an empty array

Example 1:
  Input: numCourses = 2, prerequisites = [[1,0]]
  Output: [0,1]

Example 2:
  Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
  Output: [0,2,1,3]

Example 3:
  Input: numCourses = 1, prerequisites = []
  Output: [0]


Constraints:
 - 1 <= numCourses <= 2000
 - 0 <= prerequisites.length <= numCourses * (numCourses - 1)
 - prerequisites[i].length == 2
 - 0 <= ai, bi < numCourses
 - ai != bi
 - All the pairs [ai, bi] are distinct.

"""

class Solution:
    # Track State
    UNVISITED = 0
    CURRENT = 1
    VISITED = 2

    isPossible = True

    def findOrder(self, numCourses, prerequisites):
        # Create a (dict) graph for the prerequisites, key being the preqNode, val's being the sequentially-next course
        self.preqs = {}
        for [ai, bi] in prerequisites:
            if bi in self.preqs:
                self.preqs[bi].append(ai)
            else:
                self.preqs[bi] = [ai]
        print(f"preqs = {self.preqs}")

        # Create a (list) graph to track if the selected node has been visited or not
        self.state = [self.UNVISITED for k in range(numCourses)]
        print(f"state = {self.state}")

        # Start traversing the graph and populate orderedCourses list
        self.orderedCourses = []
        for c in range(numCourses):
            if self.state[c] == self.UNVISITED:
                self.DFS(c)

        # Return empty array if not possible
        if self.isPossible:
            return self.orderedCourses[::-1]
        else:
            return []
    
    def DFS(self, node):
        # Exit if this graph has a cycle and is not possible
        if not self.isPossible:
            return
        
        self.state[node] = self.CURRENT
        # DFS for all sequentially-next courses
        if node in self.preqs:
            for course in self.preqs[node]:
                if self.state[course] == self.UNVISITED:
                    self.DFS(course)
                # If the sequentially-next course is currently being investigated, then we have a cycle in the graph
                elif self.state[course] == self.CURRENT:
                    self.isPossible = False

        # Recursion ends
        self.state[node] = self.VISITED
        self.orderedCourses.append(node)

'''
Time Complexity: O(V + E)
  Since we iterate thru the graph and visit each node(V) and each preq(E) once
Space Complexity: O(V + E) = O(preqs[E]) + O(states[V]) + O(orderedCourses [V])
'''

# Example1
nC = 2; preqs = [[1,0]]  # Output: [0,1]

# Example2
nC = 4; preqs = [[1,0],[2,0],[3,1],[3,2]]  # Output: [0, 2, 1, 3]

# Example3
nC = 1; preqs = []  # Output: [0]

# Example4
nC = 2; preqs = [[0,1]]

s = Solution()
s.findOrder(nC, preqs)
