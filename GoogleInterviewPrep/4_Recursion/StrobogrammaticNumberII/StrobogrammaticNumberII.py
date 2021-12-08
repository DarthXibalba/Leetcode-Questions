"""
Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Ex1:
  Input: n = 1
  Output: ["0", "1", "8"]

Ex2:
  Input: n = 2
  # Pairs = ["00", "11", "69", "88", "96"]

  Output: ["11", "69", "88", "96"]

Ex3:
  Input: n = 3
  Pairs: ["000", "010", "080",
          "101", "111", "181",
          "609", "619", "689",
          "808", "818", "888",
          "906", "916", "986"]

  Output: ["101", "111", "181",
           "609", "619", "689",
           "808", "818", "888",
           "906", "916", "986"]

Ex4:
  Input: n = 4
  Pairs: ["0000", "0110", "0690", "0880", "0960"
          "1001", "1111", "1691", "1881", "1961",
          "6009", "6119", "6699", "6889", "6969",
          "8008", "8118", "8698", "8888", "8968",
          "9006", "9116", "9696", "9886", "9966"]

  Output: ["1001", "1111", "1691", "1881", "1961",
           "6009", "6119", "6699", "6889", "6969",
           "8008", "8118", "8698", "8888", "8968",
           "9006", "9116", "9696", "9886", "9966"]

Constraints:
 - 1 <= n <= 14
"""

class Solution:
    stroboDigitsMap = {
        "0": "0",
        "1": "1",
        "6": "9",
        "8": "8",
        "9": "6"
    }

    def findStrobogrammatic(self, n):
        if n == 1:
            return self.findStroboStrings(1)
        else:
            return [s for s in self.findStroboStrings(n) if (s[0] != "0")]

    def findStroboStrings(self, n):
        stroboList = []
        if n == 1:
            for s in self.stroboDigitsMap:
                if s == self.stroboDigitsMap[s]:
                    stroboList.append(s)
        elif n == 2:
            for s in self.stroboDigitsMap:
                t = self.stroboDigitsMap[s]
                stroboList.append(s+t)
        else:
            stroboList_n2 = self.findStroboStrings(n-2)
            for s in self.stroboDigitsMap:
                t = self.stroboDigitsMap[s]
                for s2 in stroboList_n2:
                    stroboList.append(s+s2+t)
        return stroboList
                