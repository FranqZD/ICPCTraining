using System;
using static System.Console;
namespace Filter
{
class Program
{
static void Main (string[] args)
{
    int CantNums = int.Parse(Console.ReadLine());
        String[] numeros = Console.ReadLine().Split(' ');

        for(int i = 0;i<numeros.Length;i++)
        {
            if(int.Parse(numeros[i])%2==0){
                Console.WriteLine(numeros[i]);
            }
        }
}
}
}