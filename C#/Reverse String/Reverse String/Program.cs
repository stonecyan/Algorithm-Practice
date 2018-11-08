using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Reverse_String
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Type in a string: ");
            string word = Console.ReadLine();
            int i;
            string reverse = "";
            int length = word.Length - 1;
            for (i=length; i>=0; i--)
            {
                reverse += word[i];
            }
            Console.WriteLine(reverse);
            Console.ReadLine();
        }
    }
}
