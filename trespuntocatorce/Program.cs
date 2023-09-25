using System;
using static System.Console;
namespace trespuntocatorce
{
class Program
{
static void Main (string[] args)
{
    string pi = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679";
    int Decimales=int.Parse(ReadLine());

    for(int i = 0;i<=Decimales;i++){
        if(i==1){
            Console.Write(".");
        }
        Write(pi[i]);
    }

}
}
}