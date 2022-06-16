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

        public int[] TwoSum(int[] nums, int target)
        {
            var result = TwoSum_BruteForce(nums, target);
            return result;
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
