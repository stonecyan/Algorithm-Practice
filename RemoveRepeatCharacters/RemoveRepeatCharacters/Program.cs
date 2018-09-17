using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RemoveRepeatCharacters
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("Input a string.");
            string word = Console.ReadLine();
            int i, j;
            string singleword = "";
            singleword += word[0];

            for (i = 1; i < word.Length; i++)
            {
                for(j=0; j<singleword.Length; j++)
                {
                    if (word[i] == singleword[j])
                    {
                        break;
                    }
                    if(j==singleword.Length-1)
                    {
                        singleword += word[i];
                    }
                }
            }
            Console.WriteLine(singleword);
            Console.ReadLine();
        }
    }
}
