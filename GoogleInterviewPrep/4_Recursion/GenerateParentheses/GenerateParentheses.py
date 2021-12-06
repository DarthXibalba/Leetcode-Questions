"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Ex2:
  Input: n = 1
  Output: ["()"]

Ex3:
  Input: n = 2
  Output: ["(())", "()()"]

Ex1:
  Input: n = 3
  Output: ["((()))","(()())","(())()","()(())","()()()"]

Constraints:
 - 1 <= n <= 8
"""

class Solution:
    # Create a dictionary to reuse generated parenthesis
    genParDict = { 1 : ["()"], 2 : ["(())", "()()"] }

    def generateParenthesis(self, n):
        for i in range(n):
            self.generateNewParenthesis(i+1)  # Add 1 due to 0-index
        return self.genParDict[n]

    def generateNewParenthesis(self, n):
        if n in self.genParDict:
            return
        # Generate the newly requested set of parenthesis (n)
        else:
            pList = []

            # FIRST IN SET
            # Generate all Enclosed Sets of parenthesis
            for p in self.genParDict[n-1]:
                pList.append(f"({p})")

            # Generate all Permutation Sets of parenthesis
            # n = 3, 1*2
            # n = 4, 2*2
            # n = 5, 3*2
            # n = 6, 3*3
            # n = 7, 4*3
            # n = 8, 4*4
            # n = x, int(x/2)*int((x+1)/2)
            if n > 2:
                pList_1 = self.genParDict[int(n/2)]
                pList_2 = self.genParDict[int((n+1)/2)]
                #print(f"pList_1 = {pList_1}")
                #print(f"pList_2 = {pList_2}")

                for set_1 in pList_1:
                    for set_2 in pList_2:
                        newPar = f"{set_1}{set_2}"
                        if not (newPar in pList):
                            pList.append(newPar)
                            #print(f"newPar = {newPar}")

                # Do the inverse order as well
                for set_2 in pList_2:
                    for set_1 in pList_1:
                        newPar = f"{set_2}{set_1}"
                        if not (newPar in pList):
                            pList.append(newPar)
                            #print(f"newPar = {newPar}")

            self.genParDict[n] = pList


# Example2
Solution().generateParenthesis(1)  # Output: ["()"], len = 1
Solution().generateParenthesis(2)  # Output: ["(())", "()()"], len = 2
Solution().generateParenthesis(3)  # Output: ["((()))","(()())","(())()","()(())","()()()"], len = 5
Solution().generateParenthesis(4)  # len = 9
Solution().generateParenthesis(5)  # len = 25
Solution().generateParenthesis(6)  # len = 50
Solution().generateParenthesis(7)  # len = 136
Solution().generateParenthesis(8)  # len = 217