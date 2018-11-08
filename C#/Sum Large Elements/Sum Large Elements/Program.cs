using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sum_Large_Elements
{
    class Program
    {
        static void Main(string[] args)
        {
            long[] array = new long[] { 16, 32, 64, 128, 256 };
            int i;
            long sum = 0;

            for (i=0; i<array.Length; i++)
            {
                sum += array[i];
            }

            Console.WriteLine(sum);
            Console.ReadLine();
        }
    }
}
