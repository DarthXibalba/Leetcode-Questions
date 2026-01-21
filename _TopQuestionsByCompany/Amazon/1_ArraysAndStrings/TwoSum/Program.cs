using System;

namespace TwoSum
{
    public class Solution
    {
        public int[] TwoSum_BruteForce(int[] nums, int target)
        {
            for (int i = 0; i < nums.Count(); i++)
            {
                for (int j = i + 1; j < nums.Count(); j++)
                {
                    if (nums.ElementAt(i) + nums.ElementAt(j) == target)
                    {
                        return new int[]{i,j};
                    }
                }
            }
            return new int[]{};
        }

        public int[] TwoSum_Optimal1(int[] nums, int target)
        {
            // Create a hashmap to store elements & their respective indices
            var hashmap = new Dictionary<int, int>();
            for (int i = 0; i < nums.Count(); i++)
            {
                hashmap[nums.ElementAt(i)] = i; // This overwrites if there is a duplicate value
            }
            for (int i = 0; i < nums.Count(); i++)
            {
                var compliment = target - nums.ElementAt(i);
                // Make sure that hashmap[compliment] doesn't just match to itself
                if (hashmap.ContainsKey(compliment) && hashmap[compliment] != i)
                {
                    return new int[]{i, hashmap[compliment]};
                }
            }
            return new int[]{};
        }

        public int[] TwoSum_Optimal2(int[] nums, int target)
        {
            // Create hashmaps to store elements with their respective indices, as well as the elements compliments
            var hashmap = new Dictionary<int, int>();
            for (int i = 0; i < nums.Count(); i++)
            {
                // Check to see if compliment already exists in hashmap
                var n = nums.ElementAt(i);
                var compliment = target - n;
                if (hashmap.ContainsKey(compliment))
                {
                    return new int[]{hashmap[compliment], i};
                }
                hashmap[n] = i;
            }
            return new int[]{};
        }

        public int[] TwoSum(int[] nums, int target, int optLvl = 3)
        {
            if (optLvl == 1)
            {
                return TwoSum_BruteForce(nums, target);
            }
            else if (optLvl == 2)
            {
                return TwoSum_Optimal1(nums, target);
            }
            else
            {
                return TwoSum_Optimal2(nums, target);
            }
        }
    }

    static class Program
    {
        static void printResult(int exNum, int[] result)
        {
            string output = $"Example #{exNum}\n[";
            foreach (int i in result)
            {
                output += $"{i},";
            }
            // Remove last character
            output = output.Remove(output.Length-1,1) + "]";
            Console.WriteLine(output);
        }

        static void Main(string[] args)
        {
            // Declare inputs
            var nums = new List<int[]>{
                new int[]{2,7,11,15},
                new int[]{3,2,4},
                new int[]{3,3}
            };
            var targets = new List<int>{9,6,6};
            // Compute
            var sln = new Solution();
            var result = new List<int[]>();
            for (int i = 0; i < nums.Count(); i++)
            {
                var n = nums.ElementAt(i);
                var t = targets.ElementAt(i);
                result.Add(sln.TwoSum(n, t));
            }
            // Display output
            for (int i = 0; i < result.Count(); i++)
            {
                printResult(i+1, result.ElementAt(i));
            }
        }
    }
}
