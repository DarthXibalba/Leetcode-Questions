using System;

namespace MostCommonWords
{
    public class Solution
    {
        public string MostCommonWords_old(string paragraph, string[] banned)
        {
            // Trim symbols from paragraph and convert to lowercase
            string symbols = "!?',;.";
            string parsed_paragraph = "";
            paragraph = paragraph.ToLower();
            // Trim symbols from paragraph
            for (int i = 0; i < paragraph.Length; i++)
            {
                if (!symbols.Contains(paragraph.ElementAt(i)))
                {
                    parsed_paragraph += paragraph.ElementAt(i);
                }
                else
                {
                    parsed_paragraph += " ";
                }
            }
            // Hash every word to keep count
            string mcw = "";
            int mcwCount = 0;
            Dictionary<string, int> wordCount = new Dictionary<string, int>();
            foreach (var word in parsed_paragraph.Split(" "))
            {
                // Add "" to banned list of words to prevent it from being stored in the dictionary
                if (!banned.Contains(word) && word != "")
                {
                    if (wordCount.ContainsKey(word))
                    {
                        wordCount[word] += 1;
                    }
                    else
                    {
                        wordCount[word] = 1;
                    }
                    if (wordCount[word] > mcwCount)
                    {
                        mcwCount = wordCount[word];
                        mcw = word;
                    }
                }
            }
            return mcw;
        }

        public string MostCommonWords(string paragraph, string[] banned)
        {
            string symbols = "!?',;. ";
            string wordBuffer = "";
            string mcw = "";
            int mcwCount = 0;
            Dictionary<string, int> wordCount = new Dictionary<string, int>();
            for (int i = 0; i < paragraph.Length; i++)
            {
                char c = paragraph.ElementAt(i);
                // if the character is a valid character (letter), then add it to the buffer
                if (!symbols.Contains(c))
                {
                    wordBuffer += c;
                }
                // parse word if a symbol or end of string is encountered
                if (symbols.Contains(c) || i == paragraph.Length - 1)
                {
                    wordBuffer = wordBuffer.ToLower();
                    // only add word to dictionary if it's not empty
                    if (wordBuffer != "" && !banned.Contains(wordBuffer))
                    {
                        if (wordCount.ContainsKey(wordBuffer))
                        {
                            wordCount[wordBuffer] += 1;
                        }
                        else
                        {
                            wordCount[wordBuffer] = 1;
                        }
                        // check and store if max count
                        if (wordCount[wordBuffer] > mcwCount)
                        {
                            mcwCount = wordCount[wordBuffer];
                            mcw = wordBuffer;
                        }
                    }
                    // reset wordbuffer
                    wordBuffer = "";
                }
            }
            return mcw;
        }
    }

    public static class Program
    {
        public static void PrintOutput(List<string> paragraphs, List<string[]> banned_words, List<string> results)
        {
            string output = "";
            for (int i = 0; i < paragraphs.Count(); i++)
            {
                output += $"Paragraph: {paragraphs.ElementAt(i)}";
                output += $"\nBanned Words: [";
                foreach (var word in banned_words.ElementAt(i))
                {
                    output += $"{word},";
                }
                output += $"]\nResult: {results.ElementAt(i)}\n\n";
            }
            Console.WriteLine(output);
        }

        public static void Main(string[] args)
        {
            // Declare inputs
            var paragraph_list = new List<string>
            {
                "Bob hit a ball, the hit BALL flew far after it was hit.",
                "a.",
                "Bob. hIt, baLl"
            };
            var banned_list = new List<string[]>
            {
                new string[]{"hit"},
                new string[]{},
                new string[]{"bob", "hit"}
            };
            // Compute
            var sln = new Solution();
            var result_list = new List<string>();
            for (int i = 0; i < paragraph_list.Count(); i++)
            {
                result_list.Add(sln.MostCommonWords(paragraph_list.ElementAt(i), banned_list.ElementAt(i)));
            }
            // Display output
            PrintOutput(paragraph_list, banned_list, result_list);
        }
    }
}