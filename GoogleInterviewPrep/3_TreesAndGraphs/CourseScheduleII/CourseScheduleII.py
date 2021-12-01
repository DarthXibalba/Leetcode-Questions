"""
There are a total of numCourses courses you have to take, labeled from 0 to (numCourses-1).
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
 - For example, the pair [0, 1] indicates that to take course 0 you have to first take course 1

Return the ordering of courses you should take to finish all courses.
 - If there are many valid answers, return any of them.
 - If it is impossible to finish all courses, return an empty array

Example 1:
  Input: numCourses = 2, prerequisites =[[1,0]]
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
    def findOrder(self, numCourses, prerequisites):
        preqs = {}
        # Init preqs
        for i in range(numCourses):
            preqs[i] = []

        # Populate preqs
        for [ai, bi] in prerequisites:
            preqs[bi].append(ai)

        # Create CourseSchedule list
        schedule = []
        for i in range(numCourses):
            # Append course i if not already in schedule
            if not (i in schedule):
                schedule.append(i)
            # Append preqs[i] if not emptyList
            if preqs[i] != []:
                for j in range(len(preqs[i])):
                    # Append preqs[i][j] if not already in schedule
                    if not (preqs[i][j] in schedule):
                        schedule.append(preqs[i][j])
        return schedule


# Example1
nC = 1; preqs = [[1,0]]  # Output: [0,1]

# Example2
nC = 4; preqs = [[1,0],[2,0],[3,1],[3,2]]  # Output: [0, 1, 2, 3]

# Example3
nC = 1; preqs = []  # Output: [0]

s = Solution()
s.findOrder(nC, preqs)