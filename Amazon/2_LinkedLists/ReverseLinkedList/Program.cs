using System;

namespace ReverseLinkedList
{
    public class ListNode
    {
        public int val;
        public ListNode next;
        public ListNode(int val = 0, ListNode next = null)
        {
            this.val = val;
            this.next = next;
        }
    }

    public class Solution
    {
        public ListNode ReverseListIterative(ListNode head)
        {
            if (head == null)
            {
                return null;
            }
            ListNode revHead = new ListNode(head.val);
            while (head.next != null)
            {
                head = head.next;
                revHead = new ListNode(head.val, revHead);
            }
            return revHead;
        }

        public ListNode ReverseListRecursive(ListNode head)
        {
            if (head == null || head.next == null)
            {
                return head;
            }
            else
            {
                ListNode prevNode = ReverseListRecursive(head.next);
                head.next.next = head;
                head.next = null;
                return prevNode;
            }
        }

        public ListNode ReverseList(ListNode head, int mode = 0)
        {
            if (mode == 0)
            {
                return ReverseListIterative(head);
            }
            else
            {
                return ReverseListRecursive(head);
            }
        }

        public ListNode CreateLinkedList(int[] nums, int i = 0)
        {
            if (i < nums.Count() - 1)
            {
                return new ListNode(nums[i], CreateLinkedList(nums, i+1));
            }
            else
            {
                return new ListNode(nums[i]);
            }
        }
    }

    public static class Program
    {
        public static void PrintLinkedList(ListNode node)
        {
            if (node != null)
            {
                string output = $"{node.val}->";
                while (node.next != null)
                {
                    node = node.next;
                    output += $"{node.val}->";
                }
                Console.WriteLine(output);
            }
            else
            {
                Console.WriteLine("[]");
            }
        }

        public static void PrintOutput(List<ListNode> orig_head, List<ListNode> rev_head)
        {
            for (int i = 0; i < orig_head.Count(); i++)
            {
                PrintLinkedList(orig_head.ElementAt(i));
                PrintLinkedList(rev_head.ElementAt(i));
            }
        }

        public static void Main(string[] args)
        {
            // Declare inputs
            var sln = new Solution();
            var head_list = new List<ListNode>
            {
                sln.CreateLinkedList(new int[]{1,2,3,4,5}),
                sln.CreateLinkedList(new int[]{1,2}),
                null
            };
            var rev_list = new List<ListNode>();
            // Compute
            foreach (var head in head_list)
            {
                rev_list.Add(sln.ReverseList(head));
            }
            // Display output
            PrintOutput(head_list, rev_list);
        }
    }
}