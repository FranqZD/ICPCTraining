using System;
using static System.Console;
namespace Code
{
class Program
{
static void Main (string[] args)
{
    int cantNums = 0;
    cantNums = Int32.Parse(Console.ReadLine());
    string[][] numeros = new string[cantNums][];
    for (int i = 0; i < cantNums; i++)
    {
        numeros[i]=Console.ReadLine().Split(' ');        
    } 
    for (int i = 0; i < cantNums; i++)
    {
        
        int a=int.Parse(numeros[i][0]);
        int b=int.Parse(numeros[i][1]);
        int c=int.Parse(numeros[i][2]);
        if(c<b && c>a || c>b && c<a ){
            Console.WriteLine(c);
        }else if(b<c && b>a || b>c && b<a) {
            Console.WriteLine(b);
        }else{
            Console.WriteLine(a);
        }
    }
}
}
}
