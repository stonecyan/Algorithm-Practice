using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Odd_Sum
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] array = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
            int i;
            int sum = 0;

            for (i=0; i<array.Length; i++)
            {
                if (array[i]%2!=0)
                {
                    sum += array[i];
                }
            }

            Console.WriteLine(sum);
            Console.ReadLine();
        }
    }
}
