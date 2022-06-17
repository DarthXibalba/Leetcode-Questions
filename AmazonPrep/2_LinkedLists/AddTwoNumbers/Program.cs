using System;

namespace AddTwoNumbers
{
    public class ListNode
    {
        public int val;
        public ListNode next;
        public ListNode(int val=0, ListNode next=null)
        {
            this.val = val;
            this.next = next;
        }
    }

    public class Solution
    {
        // Create a ListNode out of an int[]
        public ListNode CreateLinkedList(int[] nums, int i = 0)
        {
            if (i < nums.Count() - 1)
            {
                return new ListNode(nums[i], CreateLinkedList(nums, i+1));
            }
            else
            {
                return new ListNode(nums[i], null);;
            }
        }        

        public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
        {
            // Add first set of nodes
            int sum = l1.val + l2.val;
            int remainder = sum % 10;
            int carryover = sum / 10;
            var result = new ListNode(remainder);
            var head_result = result;
            // Iterate until we reach the end of one of the lists
            while (l1.next != null && l2.next != null)
            {
                l1 = l1.next;
                l2 = l2.next;
                sum = l1.val + l2.val + carryover;
                remainder = sum % 10;
                carryover = sum / 10;
                result.next = new ListNode(remainder);
                result = result.next;
            }
            // Iterate to the end both lists
            while (l1.next != null)
            {
                l1 = l1.next;
                sum = l1.val + carryover;
                remainder = sum % 10;
                carryover = sum / 10;
                result.next = new ListNode(remainder);
                result = result.next;
            }
            while (l2.next != null)
            {
                l2 = l2.next;
                sum = l2.val + carryover;
                remainder = sum % 10;
                carryover = sum / 10;
                result.next = new ListNode(remainder);
                result = result.next;
            }        
            if (carryover > 0)
            {
                result.next = new ListNode(carryover);
            }    
            return head_result;
        }

        // ----- Helper Functions -----
        //public ListNode ReverseLinkedList(ListNode origNode)
        //{
        //    var revNode = new ListNode(origNode.val, null);
        //    while (origNode.next != null)
        //    {
        //        origNode = origNode.next;
        //        revNode = new ListNode(origNode.val, revNode);
        //    }
        //    return revNode;
        //}
    }

    static class Program
    {
        public static void PrintLinkedList(ListNode node)
        {
            string output = $"{node.val}->";
            while (node.next != null)
            {
                node = node.next;
                output += $"{node.val}->";
            }
            Console.WriteLine(output);
        }

        static void PrintOutput(List<ListNode> LL1, List<ListNode> LL2, List<ListNode> LLR)
        {
            for (int i = 0; i < LL1.Count(); i++)
            {
                PrintLinkedList(LL1.ElementAt(i));
                PrintLinkedList(LL2.ElementAt(i));
                PrintLinkedList(LLR.ElementAt(i));
            }
        }

        static void Main(string[] args)
        {
            var sln = new Solution();
            // Declare inputs
            var l1_list = new List<ListNode> {
                sln.CreateLinkedList(new int[]{2,4,3}),
                sln.CreateLinkedList(new int[]{0}),
                sln.CreateLinkedList(new int[]{9,9,9,9,9,9,9})
            };
            var l2_list = new List<ListNode> {
                sln.CreateLinkedList(new int[]{5,6,4}),
                sln.CreateLinkedList(new int[]{0}),
                sln.CreateLinkedList(new int[]{9,9,9,9})
            };
            // Compute
            var result_list = new List<ListNode>();
            for (int i = 0; i < l1_list.Count(); i++)
            {
                var l1 = l1_list.ElementAt(i);
                var l2 = l2_list.ElementAt(i);
                result_list.Add(sln.AddTwoNumbers(l1, l2));
            }
            // Display output
            PrintOutput(l1_list, l2_list, result_list);
        }
    }
}
