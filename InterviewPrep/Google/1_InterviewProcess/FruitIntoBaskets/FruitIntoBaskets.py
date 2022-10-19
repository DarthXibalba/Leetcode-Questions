"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
- You only have 2 baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
- Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
- Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array fruits, return the maximum number of fruits you can pick.

Example1:
I: fruits = [1,2,1]
O: 3
Explanation: We can pick from all trees

Example2:
I: fruits = [0,1,2,2]
O: 3
Explanation: We can pick from trees [1,2,2]

Example3:
I: fruits = [1,2,3,2,2]
O: 4
Explanation: We can pick from trees [2,3,2,2]

Constraints:
- 1 <= fruits.length <= 10^5
- 0 <= fruits[i] < fruits.length
"""

class Solution:
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        int last_fruit = -1
        int second_last_fruit = -1
        int last_fruit_count = 0
        int current_count = 0
        int max = 0

        for f in fruits:
            if (f != last_fruit) and (f != second_last_fruit):
                current_count += 1
            else:
                current_count = last_fruit_count + 1

            if (f == last_fruit) or (f == second_last_fruit):
                pass