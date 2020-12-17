
/*
 * If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
 * there are exactly three solutions for p = 120.
 *
 * {20,48,52}, {24,45,51}, {30,40,50}
 *
 * For which value of p ≤ 1000, is the number of solutions maximised?
 */

using System;
using System.Collections.Generic;
using System.Net.Security;

public class P039
{
    private static int PythagoreanTheorem(int a, int b)
    {
        return (int)Math.pow(a, 2) + (int)Math.Pow(b, 2);
    }

    //brute force solution
    private static List<List<int>> SideLengths(int perimeter)
    {
        var side_lengths = new List<List<int>>();

        bool out_valid = true;
        bool in_valid = true;

        int a = 3;
        int b = 3;
        int c = 0;
        while(out_valid)
        {
            b = a;
            while(in_valid)
            {
                c = perimeter - (a + b);
                if(c < (a + b))
                {
                    in_valid = false;
                }
                else if(PythagoreanTheorem(a,b) == (int)Math.Pow(c,2))
                {
                    var valid_solution = new List<int> { a, b, c };
                    side_lengths.Add(valid_solution);
                }
                b++;
            }
            if(a > (int)(perimeter/3))
            {
                out_valid = false;
            }
            a++;

        }
    }

    public static void TestSideLengths(int p)
    {
        Console.WriteLine(SideLengths(p));
    }

	static void Main()
    {
        TestSideLengths(120);
    }
}