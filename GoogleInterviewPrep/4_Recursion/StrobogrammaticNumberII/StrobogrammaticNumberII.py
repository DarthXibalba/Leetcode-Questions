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
          "808", "818", "888"]

  Output: ["101", "111", "181",
           "808", "818", "888"]

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
    def findStrobogrammatic(self, n)
        return list[str]